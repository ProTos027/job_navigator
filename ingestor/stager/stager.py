from ingestor.stager.scout import scout
from ingestor.stager.entry_operator import insert_jobs

def stage_jobs():
    
    # Fetch jobs
    print("fetching jobs...")
    jobs= scout()
    print(f"fetched n jobs.")
    
    # Insert jobs into staging table
    print("inserting jobs into staging table...")
    insert_jobs(jobs)
    print("jobs inserted successfully.")

stage_jobs()