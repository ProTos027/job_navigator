from ingestor.transformer.loader import load_normed
from ingestor.transformer.title_handler import title_handler
from ingestor.transformer.picker import fetch_jobs, setup_tables
from ingestor.transformer.desc_handler import desc_section_handler
from ingestor.transformer.preprocesser import process_basic, sectionalize

TITLE_BATCH_SIZE= None
DESC_BATCH_SIZE= None
FETCH_SIZE= None

job_gen= fetch_jobs(FETCH_SIZE)

def process(jobs):
    # preprocess jobs
    # handle preprocessed data
    # load normalized data
    pass
    
def transformer():
            
    # setup tables
    print("setting up tables...")
    setup_tables()
    print("tables set up successfully.")

    while(True):
        
        # fetch job batches
        print("fetching job batches...")
        jobs= None
        print(f"fetched n jobs this batch.")
        
        if not jobs:
            print("no more jobs to process. exiting.")
            break
        
        # process batch
        print("processing fetched batch...")
        process(jobs)
        print("batch processed successfully.")
      
transformer()