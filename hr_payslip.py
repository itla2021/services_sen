from config import *
from base import ProcessBase
import numpy as np


class ProcessHrPayslip(ProcessBase):
    def __init__(self, df, data_types=hr_payslip_data_types):
        self.struct_id = self.replace_values(df['struct_id'].to_list(), data_types["struct_id"])
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.number = self.replace_values(df['number'].to_list(), data_types["number"])
        self.employee_id = self.replace_values(df['employee_id'].to_list(), data_types["employee_id"])
        self.payslip_period = self.replace_values(df['payslip_period'].to_list(), data_types["payslip_period"])
        self.date_from = self.replace_values(df['date_from'].to_list(), data_types["date_from"])
        self.date_to = self.replace_values(df['date_to'].to_list(), data_types["date_to"])
        self.is_mobile_public = self.replace_values(df['is_mobile_public'].to_list(), data_types["is_mobile_public"])
        self.is_recall = self.replace_values(df['is_recall'].to_list(), data_types["is_recall"])
        self.year_of_tax_finalization = self.replace_values(df['year_of_tax_finalization'].to_list(),
                                                            data_types["year_of_tax_finalization"])
        self.employee_template_id = self.replace_values(df['employee_template_id'].to_list(),
                                                        data_types["employee_template_id"])
        self.is_internal = self.replace_values(df['is_internal'].to_list(), data_types["is_internal"])
        self.project_id = self.replace_values(df['project_id'].to_list(), data_types["project_id"])
        self.department_id = self.replace_values(df['department_id'].to_list(), data_types["department_id"])
        self.division_department_id = self.replace_values(df['division_department_id'].to_list(),
                                                          data_types["division_department_id"])
        self.contract_id = self.replace_values(df['contract_id'].to_list(), data_types["contract_id"])
        self.partner_id = self.replace_values(df['partner_id'].to_list(), data_types["partner_id"])
        self.partner_customer_id = self.replace_values(df['partner_customer_id'].to_list(),
                                                       data_types["partner_customer_id"])
        self.partner_customer_code = self.replace_values(df['partner_customer_code'].to_list(),
                                                         data_types["partner_customer_code"])
        self.partner_customer_email = self.replace_values(df['partner_customer_email'].to_list(),
                                                          data_types["partner_customer_email"])
        self.area_id = self.replace_values(df['area_id'].to_list(), data_types["area_id"])
        self.store_id = self.replace_values(df['store_id'].to_list(), data_types["store_id"])
        self.department_customer_id = self.replace_values(df['department_customer_id'].to_list(),
                                                          data_types["department_customer_id"])
        self.job_id = self.replace_values(df['job_id'].to_list(), data_types["job_id"])
        self.job_position_id = self.replace_values(df['job_position_id'].to_list(), data_types["job_position_id"])
        self.official_joining_date = self.replace_values(df['official_joining_date'].to_list(),
                                                         data_types["official_joining_date"])
        self.is_new_employee = self.replace_values(df['is_new_employee'].to_list(), data_types["is_new_employee"])
        self.is_resigned_employee = self.replace_values(df['is_resigned_employee'].to_list(),
                                                        data_types["is_resigned_employee"])
        self.bank_account_holder = self.replace_values(df['bank_account_holder'].to_list(),
                                                       data_types["bank_account_holder"])
        self.bank_account_number = self.replace_values(df['bank_account_number'].to_list(),
                                                       data_types["bank_account_number"])
        self.bank_abbreviation_name = self.replace_values(df['bank_abbreviation_name'].to_list(),
                                                          data_types["bank_abbreviation_name"])
        self.bank_name = self.replace_values(df['bank_name'].to_list(), data_types["bank_name"])
        self.si_code = self.replace_values(df['si_code'].to_list(), data_types["si_code"])
        self.salary_receiption_method = self.replace_values(df['salary_receiption_method'].to_list(),
                                                            data_types["salary_receiption_method"])

    def to_numpy(self):
        return np.array([
            self.struct_id, self.name, self.number,
            self.employee_id, self.payslip_period,
            self.date_from, self.date_to,
            self.is_mobile_public, self.is_recall,
            self.year_of_tax_finalization, self.employee_template_id,
            self.is_internal, self.project_id,
            self.department_id, self.division_department_id,
            self.contract_id, self.partner_id,
            self.partner_customer_id, self.partner_customer_code,
            self.partner_customer_email, self.area_id,
            self.store_id, self.department_customer_id,
            self.job_id, self.job_position_id,
            self.official_joining_date, self.is_new_employee,
            self.is_resigned_employee, self.bank_account_holder,
            self.bank_account_number, self.bank_abbreviation_name,
            self.bank_name, self.si_code,
            self.salary_receiption_method], dtype=object).T
