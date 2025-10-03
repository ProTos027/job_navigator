def insert_benefits(conn, desc_ids, benefits):
    pass

def insert_domains(conn, other_ids, domains):
    pass

def insert_emp_types(conn, other_ids, employment_types):
    pass

def insert_regions(conn, other_ids, locations):
    pass

def insert_reqs(conn, desc_ids, skills_required, exps):
    pass

def insert_resps(conn, desc_ids, responsibilities):
    pass

def insert_specials(conn, title_ids, specializations):
    pass

def insert_techs(conn, title_ids, techs):
    pass

def insert_work_set(conn, other_ids, work_settings):
    pass

def insert_core(conn, title_ids, levels, roles, languages, salary_mins, salary_maxs, salary_currencies, salary_intervals):
    pass

def update_core(conn, job_ids, exps):
    pass
    
def load_normed(title_breakdown: list[tuple], desc_breakdown: list[tuple], others: list[tuple], salaries: list[dict]):
    
    # unpack entites
    #expand abbreviated roles and add to specializations
    # unpack desc entities
    # unpack other entities
    # insert into db
    pass