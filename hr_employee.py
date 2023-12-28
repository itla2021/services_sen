from config import *
from base import ProcessBase
import numpy as np


class ProcessHrEmployee(ProcessBase):
    def __init__(self, df, data_types=hr_employee_data_types):
        self.code = self.replace_values(df['code'].to_list(), data_types["code"])
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.active = self.replace_values(df['active'].to_list(), data_types["active"])
        self.job_position_id = self.replace_values(df['job_position_id'].to_list(), data_types["job_position_id"])
        self.job_id = self.replace_values(df['job_id'].to_list(), data_types["job_id"])
        self.company_id = self.replace_values(df['company_id'].to_list(), data_types["company_id"])
        self.employee_type = self.replace_values(df['employee_type'].to_list(), data_types["employee_type"])
        self.partner_id = self.replace_values(df['partner_id'].to_list(), data_types["partner_id"])
        self.project_id = self.replace_values(df['project_id'].to_list(), data_types["project_id"])
        self.project_policy_id = self.replace_values(df['project_policy_id'].to_list(), data_types["project_policy_id"])
        self.employee_template_id = self.replace_values(df['employee_template_id'].to_list(),
                                                        data_types["employee_template_id"])
        self.resource_id = self.replace_values(df['resource_id'].to_list(), data_types["resource_id"])
        self.joining_date = self.replace_values(df['joining_date'].to_list(), data_types["joining_date"])
        self.state = self.replace_values(df['state'].to_list(), data_types["state"])
        self.labor_category_id = self.replace_values(df['labor_category_id'].to_list(), data_types["labor_category_id"])
        self.company_department_id = self.replace_values(df['company_department_id'].to_list(),
                                                         data_types["company_department_id"])
        self.department_id = self.replace_values(df['department_id'].to_list(), data_types["department_id"])
        self.customer_emp_code = self.replace_values(df['customer_emp_code'].to_list(), data_types["customer_emp_code"])
        self.birthday = self.replace_values(df['birthday'].to_list(), data_types["birthday"])
        self.mobile = self.replace_values(df['mobile'].to_list(), data_types["mobile"])
        self.payslip_email = self.replace_values(df['payslip_email'].to_list(), data_types["payslip_email"])
        self.identification_id = self.replace_values(df['identification_id'].to_list(), data_types["identification_id"])
        self.employee_template_code = self.replace_values(df['employee_template_code'].to_list(),
                                                          data_types["employee_template_code"])

    def to_numpy(self):
        return np.array([
            self.code,
            self.name,
            self.active,
            self.job_position_id,
            self.job_id,
            self.company_id,
            self.employee_type,
            self.partner_id,
            self.project_id,
            self.project_policy_id,
            self.employee_template_id,
            self.resource_id,
            self.joining_date,
            self.state,
            self.labor_category_id,
            self.company_department_id,
            self.department_id,
            self.customer_emp_code,
            self.birthday,
            self.mobile,
            self.payslip_email,
            self.identification_id,
            self.employee_template_code,
        ], dtype=object).T
