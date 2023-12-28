from config import *
from base import ProcessBase
import numpy as np
import pandas as pd


class ProcessResourceResource(ProcessBase):
    def __init__(self, df, data_types=resource_resource_data_types):
        self.active = self.replace_values(df['active'].to_list(), data_types["active"])
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.company_id = self.replace_values(df['company_id'].to_list(), data_types["company_id"])
        self.resource_type = self.replace_values(df['resource_type'].to_list(), data_types["resource_type"])
        self.time_efficiency = self.replace_values(df['time_efficiency'].to_list(), data_types["time_efficiency"])
        self.calendar_id = self.replace_values(df['calendar_id'].to_list(), data_types["calendar_id"])
        self.create_date = self.replace_values(df['create_date'].to_list(), data_types["create_date"])
        self.create_uid = self.replace_values(df['create_uid'].to_list(), data_types["create_uid"])

    def to_numpy(self):
        return np.array([
            self.active,
            self.name,
            self.company_id,
            self.resource_type,
            self.time_efficiency,
            self.calendar_id,
            self.create_date,
            self.create_uid,
        ], dtype=object).T


# if __name__ == "__main__":
#     # ======================================================
#     #               READ DATA TO DATAFRAME
#
#     df_resource_resource = pd.read_csv(RESOURCE_RESOURCE_INPUT)
#     data = ProcessResourceResource(df_resource_resource)
#     values = data.to_numpy()[7:10] # limit data input
#
#     # ======================================================
#     #               INSERT INTO DATABASE
#
#     # Insert data to PostgreSQL database
#     data.insert_postgre(sql_command=sql_resource_resource_command, values=values)


