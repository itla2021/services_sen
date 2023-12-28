# ==============================================
#               DATA INPUT PATH
OUTPUT = "./output/"

RESOURCE_RESOURCE_INPUT = "./input/resource_resource.csv"
HR_EMPLOYEE_TEMPLATE_INPUT = "./input/hr_employee_template.csv"
HR_EMPLOYEE_INPUT = "./input/hr_employee.csv"
HR_CONTRACT_INPUT = "./input/hr_contract.csv"
HR_PAYSLIP_RUN_INPUT = "./input/hr_payslip_run.csv"
HR_PAYSLIP_INPUT = "./input/hr_payslip.csv"

# ==============================================
#               DATABASE CONNECTING
dbname = 'main_220803'
user = 'odoo'
password = 'odoo'
host = '10.10.10.24'

# ==============================================
#               SQL COMMAND

SQL_HR_EMPLOYEE_TEMPLATE_COMMAND = '''
    INSERT INTO hr_employee_template (
        company_id, old_code, code, name, active, internal,
        joining_date, birthday, mobile, payslip_email,
        identification_id
    )
    VALUES %s
    RETURNING ID, company_id, old_code, code, name, active, internal,
        joining_date, birthday, mobile, payslip_email,
        identification_id
'''

SQL_RESOURCE_RESOURCE_COMMAND = '''
    INSERT INTO resource_resource (
        active,name,company_id,resource_type,time_efficiency,calendar_id,create_date,create_uid
    )
    VALUES %s
    RETURNING ID, active,name,company_id,resource_type,time_efficiency,calendar_id, create_date, create_uid
'''

SQL_HR_EMPLOYEE_COMMAND = '''
    INSERT INTO hr_employee (
        code, name, active, job_position_id, job_id, company_id,
        employee_type, partner_id, project_id, project_policy_id,
        employee_template_id, resource_id, joining_date, state,
        labor_category_id, company_department_id, department_id,
        customer_emp_code, birthday, mobile, payslip_email,
        identification_id, employee_template_code
    )
    VALUES %s
    RETURNING ID, code, name, active, job_position_id, job_id, company_id,
        employee_type, partner_id, project_id, project_policy_id,
        employee_template_id, resource_id, joining_date, state,
        labor_category_id, company_department_id, department_id,
        customer_emp_code, birthday, mobile, payslip_email,
        identification_id, employee_template_code
'''

SQL_HR_CONTRACT_COMMAND = '''
    INSERT INTO hr_contract (
        name, employee_id, department_id, type_id, job_id,
       date_start, date_end, resource_calendar_id, wage, state,
       company_id, struct_id, schedule_pay, no_attendance, is_main,
       history_checked, is_old_contract, salary_type, gross_wage,
       other_wage, trial, priority, check_remind, check_to_office,
       check_pass, check_pass_view, is_apprenticeship_contract,
       signer_id, sign_date, project_id, code, sign_number,
       have_a_salary_agreement, is_other_contract, not_resign,
       is_official_contract, project_policy_id, employee_template_id,
       employee_template_code, salary_rule_uom_id, salary_confirmed,
       have_hard_copy, can_renew_event, from_transfer, leave_rule_id,
       leave_obligation_id, salary_13th_id, insurance_policy_id,
       other_insurance_id, contract_provision_id, other_bonus_policy_id,
       insurance_subject_id, number_of_sign, date_end_contract,
       annual_leave_increment_id, annual_leave_transfer_policy_id,
       annual_leave_payment_policy_id, responsible_for_payment_id,
       payment_policy_id, work_time_id, work_time_hours_id,
       reset_time_hours_id, provision_supplementary_id, import_uid,
       task_category_id, including_probation, date_start_probation,
       personal_income_tax_id, company_department_id, is_stopped_working,
       management_legal_entity_id, department_block_id, sent_mail,
       active, weekly_holiday_id, reset_timeoff, trial_value_uom,
       is_definite_contract, is_authorization, contract_sign_type,
       project_work_location_id, signer_user_id, trial_allowance_percent,
       create_date
    )
    VALUES %s
    RETURNING ID, name, employee_id, department_id, type_id, job_id,
       date_start, date_end, resource_calendar_id, wage, state,
       company_id, struct_id, schedule_pay, no_attendance, is_main,
       history_checked, is_old_contract, salary_type, gross_wage,
       other_wage, trial, priority, check_remind, check_to_office,
       check_pass, check_pass_view, is_apprenticeship_contract,
       signer_id, sign_date, project_id, code, sign_number,
       have_a_salary_agreement, is_other_contract, not_resign,
       is_official_contract, project_policy_id, employee_template_id,
       employee_template_code, salary_rule_uom_id, salary_confirmed,
       have_hard_copy, can_renew_event, from_transfer, leave_rule_id,
       leave_obligation_id, salary_13th_id, insurance_policy_id,
       other_insurance_id, contract_provision_id, other_bonus_policy_id,
       insurance_subject_id, number_of_sign, date_end_contract,
       annual_leave_increment_id, annual_leave_transfer_policy_id,
       annual_leave_payment_policy_id, responsible_for_payment_id,
       payment_policy_id, work_time_id, work_time_hours_id,
       reset_time_hours_id, provision_supplementary_id, import_uid,
       task_category_id, including_probation, date_start_probation,
       personal_income_tax_id, company_department_id, is_stopped_working,
       management_legal_entity_id, department_block_id, sent_mail,
       active, weekly_holiday_id, reset_timeoff, trial_value_uom,
       is_definite_contract, is_authorization, contract_sign_type,
       project_work_location_id, signer_user_id, trial_allowance_percent,
       create_date
'''

SQL_HR_PAYSLIP_RUN_COMMAND = '''
    INSERT INTO hr_payslip_run  (
       name, state, date_start, date_end, project_id,
       department_id, structure_id, hrbp_user_id, approval_type_id,
       payslip_publish_option, division_department_id,
       company_department_id, project_policy_id,
       year_of_tax_finalization, income_type, payslip_month,
       payslip_year
    )
    VALUES %s
    RETURNING ID, name, state, date_start, date_end, project_id
'''

SQL_HR_PAYSLIP_COMMAND = '''
    INSERT INTO hr_payslip  (
        struct_id, name, number, employee_id, payslip_period, date_from, date_to, is_mobile_public,
        is_recall, year_of_tax_finalization, employee_template_id, is_internal,
        project_id, department_id, division_department_id, contract_id, partner_id,
        partner_customer_id, partner_customer_code, partner_customer_email, area_id,
        store_id, department_customer_id, job_id, job_position_id, official_joining_date,
        is_new_employee, is_resigned_employee, bank_account_holder, bank_account_number,
        bank_abbreviation_name, bank_name, si_code, salary_receiption_method
    )
    VALUES %s
    RETURNING ID, struct_id, name, number, employee_id, payslip_period, date_from, date_to, is_mobile_public,
        is_recall, year_of_tax_finalization, employee_template_id, is_internal,
        project_id, department_id, division_department_id, contract_id, partner_id,
        partner_customer_id, partner_customer_code, partner_customer_email, area_id,
        store_id, department_customer_id, job_id, job_position_id, official_joining_date,
        is_new_employee, is_resigned_employee, bank_account_holder, bank_account_number,
        bank_abbreviation_name, bank_name, si_code, salary_receiption_method
'''

# ==============================================
#               DATA TYPE

hr_employee_template_data_types = {
    'company_id': int,
    'old_code': str,
    'code': str,
    'name': str,
    'active': bool,
    'internal': bool,
    'joining_date': 'datetime64[ns]',
    'birthday': 'datetime64[ns]',
    'mobile': str,
    'payslip_email': str,
    'identification_id': str
}

resource_resource_data_types = {
    'active': bool,
    'name': str,
    'company_id': int,
    'resource_type': str,
    'time_efficiency': int,
    'calendar_id': int,
    'create_date': 'datetime64[ns]',
    'create_uid': int
}

hr_employee_data_types = {
    'code': str,
    'name': str,
    'active': bool,
    'job_position_id': int,
    'job_id': int,
    'company_id': int,
    'employee_type': str,
    'partner_id': int,
    'project_id': int,
    'project_policy_id': int,
    'employee_template_id': int,
    'resource_id': int,
    'joining_date': 'datetime64[ns]',  # Consider converting to datetime later
    'state': str,
    'labor_category_id': int,
    'company_department_id': int,
    'department_id': int,
    'customer_emp_code': str,
    'birthday': 'datetime64[ns]',  # Consider converting to datetime later
    'mobile': str,
    'payslip_email': str,
    'identification_id': str,
    'employee_template_code': str
}

hr_contract_data_type = {
    'name': str,
    'employee_id': int,
    'department_id': int,
    'type_id': int,
    'job_id': int,
    'date_start': 'datetime64[ns]',
    'date_end': 'datetime64[ns]',
    'resource_calendar_id': int,
    'wage': int,
    'state': str,
    'company_id': int,
    'struct_id': int,
    'schedule_pay': str,
    'no_attendance': bool,
    'is_main': bool,
    'history_checked': bool,
    'is_old_contract': bool,
    'salary_type': str,
    'gross_wage': int,
    'other_wage': int,
    'trial': bool,
    'priority': str,
    'check_remind': bool,
    'check_to_office': bool,
    'check_pass': bool,
    'check_pass_view': bool,
    'is_apprenticeship_contract': bool,
    'signer_id': int,
    'sign_date': 'datetime64[ns]',
    'project_id': int,
    'code': str,
    'sign_number': str,
    'have_a_salary_agreement': bool,
    'is_other_contract': bool,
    'not_resign': bool,
    'is_official_contract': bool,
    'project_policy_id': int,
    'employee_template_id': int,
    'employee_template_code': str,
    'salary_rule_uom_id': int,
    'salary_confirmed': bool,
    'have_hard_copy': bool,
    'can_renew_event': bool,
    'from_transfer': bool,
    'leave_rule_id': int,
    'leave_obligation_id': int,
    'salary_13th_id': int,
    'insurance_policy_id': int,
    'other_insurance_id': int,
    'contract_provision_id': int,
    'other_bonus_policy_id': int,
    'insurance_subject_id': int,
    'number_of_sign': int,
    'date_end_contract': 'datetime64[ns]',
    'annual_leave_increment_id': int,
    'annual_leave_transfer_policy_id': int,
    'annual_leave_payment_policy_id': int,
    'responsible_for_payment_id': int,
    'payment_policy_id': int,
    'work_time_id': int,
    'work_time_hours_id': int,
    'reset_time_hours_id': int,
    'provision_supplementary_id': int,
    'import_uid': int,
    'task_category_id': int,
    'including_probation': bool,
    'date_start_probation': 'datetime64[ns]',
    'personal_income_tax_id': int,
    'company_department_id': int,
    'is_stopped_working': bool,
    'management_legal_entity_id': int,
    'department_block_id': int,
    'sent_mail': bool,
    'active': bool,
    'weekly_holiday_id': int,
    'reset_timeoff': bool,
    'trial_value_uom': str,
    'is_definite_contract': bool,
    'is_authorization': bool,
    'contract_sign_type': str,
    'project_work_location_id': int,
    'signer_user_id': int,
    'trial_allowance_percent': int,
    'create_date': 'datetime64[ns]',
}

hr_payslip_run_data_type = {
    'name': str, 'state': str, 'date_start': str, 'date_end': str,
    'project_id': int, 'department_id': int, 'structure_id': int, 'hrbp_user_id': int,
    'approval_type_id': int, 'payslip_publish_option': str, 'division_department_id': int,
    'company_department_id': int, 'project_policy_id': int, 'year_of_tax_finalization': int,
    'income_type': str, 'payslip_month': str, 'payslip_year': str
}

hr_payslip_data_types = {
    'struct_id': int, 'name': str, 'number': str, 'employee_id': int,
    'payslip_period': str, 'date_from': 'datetime64[ns]', 'date_to': 'datetime64[ns]',
    'is_mobile_public': bool, 'is_recall': bool, 'year_of_tax_finalization': int,
    'employee_template_id': int, 'is_internal': bool, 'project_id': int,
    'department_id': int, 'division_department_id': int, 'contract_id': int,
    'partner_id': int, 'partner_customer_id': int, 'partner_customer_code': str,
    'partner_customer_email': str, 'area_id': int, 'store_id': int,
    'department_customer_id': int, 'job_id': int, 'job_position_id': int,
    'official_joining_date': 'datetime64[ns]', 'is_new_employee': bool,
    'is_resigned_employee': bool, 'bank_account_holder': str, 'bank_account_number': str,
    'bank_abbreviation_name': str, 'bank_name': str, 'si_code': str,
    'salary_receiption_method': str
}

