from config import *
from base import ProcessBase
import numpy as np
import pandas as pd


class ProcessHrContact(ProcessBase):
    def __init__(self, df, data_types=hr_contract_data_type):
        self.name = self.replace_values(df['name'].to_list(), data_types["name"])
        self.employee_id = self.replace_values(df['employee_id'].to_list(), data_types["employee_id"])
        self.department_id = self.replace_values(df['department_id'].to_list(), data_types["department_id"])
        self.type_id = self.replace_values(df['type_id'].to_list(), data_types["type_id"])
        self.job_id = self.replace_values(df['job_id'].to_list(), data_types["job_id"])
        self.date_start = self.replace_values(df['date_start'].to_list(), data_types["date_start"])
        self.date_end = self.replace_values(df['date_end'].to_list(), data_types["date_end"])
        self.resource_calendar_id = self.replace_values(df['resource_calendar_id'].to_list(),
                                                        data_types["resource_calendar_id"])
        self.wage = self.replace_values(df['wage'].to_list(), data_types["wage"])
        self.state = self.replace_values(df['state'].to_list(), data_types["state"])
        self.company_id = self.replace_values(df['company_id'].to_list(), data_types["company_id"])
        self.struct_id = self.replace_values(df['struct_id'].to_list(), data_types["struct_id"])
        self.schedule_pay = self.replace_values(df['schedule_pay'].to_list(), data_types["schedule_pay"])
        self.no_attendance = self.replace_values(df['no_attendance'].to_list(), data_types["no_attendance"])
        self.is_main = self.replace_values(df['is_main'].to_list(), data_types["is_main"])
        self.history_checked = self.replace_values(df['history_checked'].to_list(), data_types["history_checked"])
        self.is_old_contract = self.replace_values(df['is_old_contract'].to_list(), data_types["is_old_contract"])
        self.salary_type = self.replace_values(df['salary_type'].to_list(), data_types["salary_type"])
        self.gross_wage = self.replace_values(df['gross_wage'].to_list(), data_types["gross_wage"])
        self.other_wage = self.replace_values(df['other_wage'].to_list(), data_types["other_wage"])
        self.trial = self.replace_values(df['trial'].to_list(), data_types["trial"])
        self.priority = self.replace_values(df['priority'].to_list(), data_types["priority"])
        self.check_remind = self.replace_values(df['check_remind'].to_list(), data_types["check_remind"])
        self.check_to_office = self.replace_values(df['check_to_office'].to_list(), data_types["check_to_office"])
        self.check_pass = self.replace_values(df['check_pass'].to_list(), data_types["check_pass"])
        self.check_pass_view = self.replace_values(df['check_pass_view'].to_list(), data_types["check_pass_view"])
        self.is_apprenticeship_contract = self.replace_values(df['is_apprenticeship_contract'].to_list(),
                                                              data_types["is_apprenticeship_contract"])
        self.signer_id = self.replace_values(df['signer_id'].to_list(), data_types["signer_id"])
        self.sign_date = self.replace_values(df['sign_date'].to_list(), data_types["sign_date"])
        self.project_id = self.replace_values(df['project_id'].to_list(), data_types["project_id"])
        self.code = self.replace_values(df['code'].to_list(), data_types["code"])
        self.sign_number = self.replace_values(df['sign_number'].to_list(), data_types["sign_number"])
        self.have_a_salary_agreement = self.replace_values(df['have_a_salary_agreement'].to_list(),
                                                           data_types["have_a_salary_agreement"])
        self.is_other_contract = self.replace_values(df['is_other_contract'].to_list(), data_types["is_other_contract"])
        self.not_resign = self.replace_values(df['not_resign'].to_list(), data_types["not_resign"])
        self.is_official_contract = self.replace_values(df['is_official_contract'].to_list(),
                                                        data_types["is_official_contract"])
        self.project_policy_id = self.replace_values(df['project_policy_id'].to_list(), data_types["project_policy_id"])
        self.employee_template_id = self.replace_values(df['employee_template_id'].to_list(),
                                                        data_types["employee_template_id"])
        self.employee_template_code = self.replace_values(df['employee_template_code'].to_list(),
                                                          data_types["employee_template_code"])
        self.salary_rule_uom_id = self.replace_values(df['salary_rule_uom_id'].to_list(),
                                                      data_types["salary_rule_uom_id"])
        self.salary_confirmed = self.replace_values(df['salary_confirmed'].to_list(), data_types["salary_confirmed"])
        self.have_hard_copy = self.replace_values(df['have_hard_copy'].to_list(), data_types["have_hard_copy"])
        self.can_renew_event = self.replace_values(df['can_renew_event'].to_list(), data_types["can_renew_event"])
        self.from_transfer = self.replace_values(df['from_transfer'].to_list(), data_types["from_transfer"])
        self.leave_rule_id = self.replace_values(df['leave_rule_id'].to_list(), data_types["leave_rule_id"])
        self.leave_obligation_id = self.replace_values(df['leave_obligation_id'].to_list(),
                                                       data_types["leave_obligation_id"])
        self.salary_13th_id = self.replace_values(df['salary_13th_id'].to_list(), data_types["salary_13th_id"])
        self.insurance_policy_id = self.replace_values(df['insurance_policy_id'].to_list(),
                                                       data_types["insurance_policy_id"])
        self.other_insurance_id = self.replace_values(df['other_insurance_id'].to_list(),
                                                      data_types["other_insurance_id"])
        self.contract_provision_id = self.replace_values(df['contract_provision_id'].to_list(),
                                                         data_types["contract_provision_id"])
        self.other_bonus_policy_id = self.replace_values(df['other_bonus_policy_id'].to_list(),
                                                         data_types["other_bonus_policy_id"])
        self.insurance_subject_id = self.replace_values(df['insurance_subject_id'].to_list(),
                                                        data_types["insurance_subject_id"])
        self.number_of_sign = self.replace_values(df['number_of_sign'].to_list(), data_types["number_of_sign"])
        self.date_end_contract = self.replace_values(df['date_end_contract'].to_list(), data_types["date_end_contract"])
        self.annual_leave_increment_id = self.replace_values(df['annual_leave_increment_id'].to_list(),
                                                             data_types["annual_leave_increment_id"])
        self.annual_leave_transfer_policy_id = self.replace_values(df['annual_leave_transfer_policy_id'].to_list(),
                                                                   data_types["annual_leave_transfer_policy_id"])
        self.annual_leave_payment_policy_id = self.replace_values(df['annual_leave_payment_policy_id'].to_list(),
                                                                  data_types["annual_leave_payment_policy_id"])
        self.responsible_for_payment_id = self.replace_values(df['responsible_for_payment_id'].to_list(),
                                                              data_types["responsible_for_payment_id"])
        self.payment_policy_id = self.replace_values(df['payment_policy_id'].to_list(), data_types["payment_policy_id"])
        self.work_time_id = self.replace_values(df['work_time_id'].to_list(), data_types["work_time_id"])
        self.work_time_hours_id = self.replace_values(df['work_time_hours_id'].to_list(),
                                                      data_types["work_time_hours_id"])
        self.reset_time_hours_id = self.replace_values(df['reset_time_hours_id'].to_list(),
                                                       data_types["reset_time_hours_id"])
        self.provision_supplementary_id = self.replace_values(df['provision_supplementary_id'].to_list(),
                                                              data_types["provision_supplementary_id"])
        self.import_uid = self.replace_values(df['import_uid'].to_list(), data_types["import_uid"])
        self.task_category_id = self.replace_values(df['task_category_id'].to_list(), data_types["task_category_id"])
        self.including_probation = self.replace_values(df['including_probation'].to_list(),
                                                       data_types["including_probation"])
        self.date_start_probation = self.replace_values(df['date_start_probation'].to_list(),
                                                        data_types["date_start_probation"])
        self.personal_income_tax_id = self.replace_values(df['personal_income_tax_id'].to_list(),
                                                          data_types["personal_income_tax_id"])
        self.company_department_id = self.replace_values(df['company_department_id'].to_list(),
                                                         data_types["company_department_id"])
        self.is_stopped_working = self.replace_values(df['is_stopped_working'].to_list(),
                                                      data_types["is_stopped_working"])
        self.management_legal_entity_id = self.replace_values(df['management_legal_entity_id'].to_list(),
                                                              data_types["management_legal_entity_id"])
        self.department_block_id = self.replace_values(df['department_block_id'].to_list(),
                                                       data_types["department_block_id"])
        self.sent_mail = self.replace_values(df['sent_mail'].to_list(), data_types["sent_mail"])
        self.active = self.replace_values(df['active'].to_list(), data_types["active"])
        self.weekly_holiday_id = self.replace_values(df['weekly_holiday_id'].to_list(), data_types["weekly_holiday_id"])
        self.reset_timeoff = self.replace_values(df['reset_timeoff'].to_list(), data_types["reset_timeoff"])
        self.trial_value_uom = self.replace_values(df['trial_value_uom'].to_list(), data_types["trial_value_uom"])
        self.is_definite_contract = self.replace_values(df['is_definite_contract'].to_list(),
                                                        data_types["is_definite_contract"])
        self.is_authorization = self.replace_values(df['is_authorization'].to_list(), data_types["is_authorization"])
        self.contract_sign_type = self.replace_values(df['contract_sign_type'].to_list(),
                                                      data_types["contract_sign_type"])
        self.project_work_location_id = self.replace_values(df['project_work_location_id'].to_list(),
                                                            data_types["project_work_location_id"])
        self.signer_user_id = self.replace_values(df['signer_user_id'].to_list(), data_types["signer_user_id"])
        self.trial_allowance_percent = self.replace_values(df['trial_allowance_percent'].to_list(),
                                                           data_types["trial_allowance_percent"])
        self.create_date = self.replace_values(df['create_date'].to_list(), data_types["create_date"])

    def to_numpy(self):
        return np.array([
            self.name,
            self.employee_id,
            self.department_id,
            self.type_id,
            self.job_id,
            self.date_start,
            self.date_end,
            self.resource_calendar_id,
            self.wage,
            self.state,
            self.company_id,
            self.struct_id,
            self.schedule_pay,
            self.no_attendance,
            self.is_main,
            self.history_checked,
            self.is_old_contract,
            self.salary_type,
            self.gross_wage,
            self.other_wage,
            self.trial,
            self.priority,
            self.check_remind,
            self.check_to_office,
            self.check_pass,
            self.check_pass_view,
            self.is_apprenticeship_contract,
            self.signer_id,
            self.sign_date,
            self.project_id,
            self.code,
            self.sign_number,
            self.have_a_salary_agreement,
            self.is_other_contract,
            self.not_resign,
            self.is_official_contract,
            self.project_policy_id,
            self.employee_template_id,
            self.employee_template_code,
            self.salary_rule_uom_id,
            self.salary_confirmed,
            self.have_hard_copy,
            self.can_renew_event,
            self.from_transfer,
            self.leave_rule_id,
            self.leave_obligation_id,
            self.salary_13th_id,
            self.insurance_policy_id,
            self.other_insurance_id,
            self.contract_provision_id,
            self.other_bonus_policy_id,
            self.insurance_subject_id,
            self.number_of_sign,
            self.date_end_contract,
            self.annual_leave_increment_id,
            self.annual_leave_transfer_policy_id,
            self.annual_leave_payment_policy_id,
            self.responsible_for_payment_id,
            self.payment_policy_id,
            self.work_time_id,
            self.work_time_hours_id,
            self.reset_time_hours_id,
            self.provision_supplementary_id,
            self.import_uid,
            self.task_category_id,
            self.including_probation,
            self.date_start_probation,
            self.personal_income_tax_id,
            self.company_department_id,
            self.is_stopped_working,
            self.management_legal_entity_id,
            self.department_block_id,
            self.sent_mail,
            self.active,
            self.weekly_holiday_id,
            self.reset_timeoff,
            self.trial_value_uom,
            self.is_definite_contract,
            self.is_authorization,
            self.contract_sign_type,
            self.project_work_location_id,
            self.signer_user_id,
            self.trial_allowance_percent,
            self.create_date], dtype=object).T
