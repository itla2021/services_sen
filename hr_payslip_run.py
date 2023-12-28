from config import *
from base import ProcessBase
import numpy as np


class ProcessHrPayslipRun(ProcessBase):
    def __init__(self, df, data_types=hr_payslip_run_data_type):
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.state = self.replace_values(df['state'].to_list(), data_types["state"])
        self.date_start = self.replace_values(df['date_start'].to_list(), data_types["date_start"])
        self.date_end = self.replace_values(df['date_end'].to_list(), data_types["date_end"])
        self.project_id = self.replace_values(df['project_id'].to_list(), data_types["project_id"])
        self.department_id = self.replace_values(df['department_id'].to_list(), data_types["department_id"])
        self.structure_id = self.replace_values(df['structure_id'].to_list(), data_types["structure_id"])
        self.hrbp_user_id = self.replace_values(df['hrbp_user_id'].to_list(), data_types["hrbp_user_id"])
        self.approval_type_id = self.replace_values(df['approval_type_id'].to_list(), data_types["approval_type_id"])
        self.payslip_publish_option = self.replace_values(df['payslip_publish_option'].to_list(),
                                                          data_types["payslip_publish_option"])
        self.division_department_id = self.replace_values(df['division_department_id'].to_list(),
                                                          data_types["division_department_id"])
        self.company_department_id = self.replace_values(df['company_department_id'].to_list(),
                                                         data_types["company_department_id"])
        self.project_policy_id = self.replace_values(df['project_policy_id'].to_list(), data_types["project_policy_id"])
        self.year_of_tax_finalization = self.replace_values(df['year_of_tax_finalization'].to_list(),
                                                            data_types["year_of_tax_finalization"])
        self.income_type = self.replace_values(df['income_type'].to_list(), data_types["income_type"])
        self.payslip_month = self.replace_values(df['payslip_month'].to_list(), data_types["payslip_month"])
        self.payslip_year = self.replace_values(df['payslip_year'].to_list(), data_types["payslip_year"])

    def to_numpy(self):
        return np.array([
            self.name, self.state, self.date_start, self.date_end,
            self.project_id, self.department_id, self.structure_id,
            self.hrbp_user_id, self.approval_type_id, self.payslip_publish_option,
            self.division_department_id, self.company_department_id,
            self.project_policy_id, self.year_of_tax_finalization,
            self.income_type, self.payslip_month, self.payslip_year
        ], dtype=object).T
