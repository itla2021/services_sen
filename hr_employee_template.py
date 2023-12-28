from config import *
from base import ProcessBase
import numpy as np


class ProcessHrEmployeeTemplate(ProcessBase):
    def __init__(self, df, data_types=hr_employee_template_data_types):
        self.company_id = self.replace_values(df['company_id'].to_list(), data_types["company_id"])
        self.old_code = self.replace_values(df['old_code'].to_list(), data_types["old_code"])
        self.code = self.replace_values(df['code'].to_list(), data_types["code"])
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.active = self.replace_values(df['active'].to_list(), data_types["active"])
        self.internal = self.replace_values(df['internal'].to_list(), data_types["internal"])
        self.joining_date = self.replace_values(df['joining_date'].to_list(), data_types["joining_date"])
        self.birthday = self.replace_values(df['birthday'].to_list(), data_types["birthday"])
        self.mobile = self.replace_values(df['mobile'].to_list(), data_types["mobile"])
        self.payslip_email = self.replace_values(df['payslip_email'].to_list(), data_types["payslip_email"])
        self.identification_id = self.replace_values(df['identification_id'].to_list(), data_types["identification_id"])

    def to_numpy(self):
        return np.array([
            self.company_id,
            self.old_code,
            self.code,
            self.name,
            self.active,
            self.internal,
            self.joining_date,
            self.birthday,
            self.mobile,
            self.payslip_email,
            self.identification_id
        ], dtype=object).T
