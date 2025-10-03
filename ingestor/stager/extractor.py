def match_metadata_batch(jobs: list[dict], model, REF_EMB, threshold=0.64):
    # gather all metadata field names and their slices
    # compute embeddings and similarities
    # determine best matches for each field name
    pass

def extract_greenhouse(job, matches: dict):
    # set listing status
    # extract fields
    # find relevant metadata based on matches
    # create and return CanonicalJob instance
    pass

def extract_ashby(job):
    
    # set listing status
    # extract fields
    # create and return CanonicalJob instance
    pass

def set_flush(val: bool):
    #set flush
    pass
    
def extractor(job, model, REF_EMB):
    # if ats is greenhouse, buffer and batch jobs
        # buffer full, process batch
            # reset buffer
    # if flush signal received, process remaining buffered jobs
    # if ats is ashby, process immediately
    pass

