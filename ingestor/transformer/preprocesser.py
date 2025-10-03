def extract_salary(jd: str)-> dict | None:
    # find invalid contexts like "bonus" nearby
    # Extract hourly salaries
    # Extract annual salary ranges
    # Extract single annual salaries
    #prefer annual
    pass

def process_basic(text: str)-> str:
    #clean string
    pass
    
def extract_tokens(descs)-> tuple[list, list]:
    # clean html tags and unescape html entities
    # identify headings and subheadings
    pass

def match_tokens(tokens, job_ids)-> tuple[dict, dict]:
    # compute embeddings and cosine similarities
    # map token to the corresponding reference label
    pass

def sort_tokens(desc, token_list)-> tuple[list, list, list]:
    # sort em according to their loc in section
    pass

def slice_sections(desc, token_list, start, end, token_map, normalized_headings):
    # extract text between two tokens and clean html tags
    # handle text after the last token
    pass

def sectionalize(descs)-> tuple[list, list]:
    # clean fallback text
    # extract salary
    # extract sections for each job desc
    # sort tokens based on their occurrence in the job desc
    # slice sections based on the sorted tokens
    # merge sections and add prefixes
    pass

def numerize(val):
    #make numeric
    pass