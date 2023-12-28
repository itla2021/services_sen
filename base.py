import numpy as np
import os
from datetime import datetime
from config import *
import psycopg2
from psycopg2 import extras
import pandas as pd


class ProcessBase:
    def replace_values(self, list_data, data_type):
        if data_type == int:
            return [self.try_int_conversion(value) if isinstance(value, (int, float)) else None for value in list_data]
        elif data_type == float:
            return [value if isinstance(value, (int, float)) else None for value in list_data]
        elif data_type == bool:
            return [value if isinstance(value, bool) else None for value in list_data]
        elif data_type == str:
            processed_values = []

            for value in list_data:
                if str(value) != 'nan' and len(str(value).split(".")) > 1:
                    # If it's a float with '.0', extract the integer part
                    if str(value).split(".")[1] == '0':
                        processed_values.append(str(value).split(".")[0])
                    else:
                        # Otherwise, keep the original string value
                        processed_values.append(str(value))
                elif str(value) == 'nan':
                    # If it's 'nan', replace with None
                    processed_values.append('')
                else:
                    # Otherwise, keep the original string value
                    processed_values.append(str(value))
            return processed_values
        elif data_type == 'datetime64[ns]':
            return [value if str(value) != 'nan' else None for value in list_data]
        else:
            return list_data

    def try_int_conversion(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def to_numpy(self):
        # Common method for converting attributes to NumPy array
        pass

    def insert_postgre(self, sql_command, values):
        """
        Insert data into PostgreSQL table.

        :param sql_command: str - SQL command for insertion.
        :param values: numpy.ndarray - NumPy array 2D containing values to be inserted.
        :return: None
        """
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=5433)

        cursor = conn.cursor()

        # Execute the SQL query with the values from the NumPy array
        extras.execute_values(cursor, sql_command, values.tolist(), page_size=len(values))

        # Commit the transaction
        conn.commit()

        # Fetch the returned IDs
        returned_ids = cursor.fetchall()

        # Print or use the returned IDs as needed
        print("Returned IDs:", returned_ids)

        column_names_str = sql_command.split("RETURNING")[1].strip()
        column_names = [name.strip() for name in column_names_str.split(',')]

        df_returned_ids = pd.DataFrame(returned_ids, columns=column_names)
        # Save the DataFrame to a CSV file
        csv_file_path = OUTPUT + self.generate_filename(sql_command)
        df_returned_ids.to_csv(csv_file_path, index=False)
        print(f"Output file save at {csv_file_path}")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    def generate_filename(self, sql_command: str):
        """
        Create csv name file
        :param sql_command: str - SQL command for insert
        :return file_name: str - Unique CSV file name
        """
        # Extract table name from SQL command
        table_name_start = sql_command.find('INSERT INTO ') + len('INSERT INTO ')
        table_name_end = sql_command.find('(', table_name_start)
        table_name = sql_command[table_name_start:table_name_end].strip()

        # Create a timestamp with the current date and time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Construct the file name
        file_name = f"{table_name}_{timestamp}.csv"

        return file_name
