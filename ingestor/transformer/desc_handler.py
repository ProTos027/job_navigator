def process(token: str):
    #clean string
    pass

def find_exp(sub: str, full: str):
    # find sentence containing the sub
    # look for range pattern first
    # look for plus pattern
    # look for single pattern
    pass

def exp_fallback(full:str)-> int|None:
    # month to year conversion
    # find plus pattern
    # find single pattern
    pass

def extract_prefix(text: str):
    # find prefix
    pass

def chunk_section(text: str, max_len: int = 500) -> list[str]:
    # get chunks
        # find closest sentence break
        # add prefix if needed
    pass

def desc_section_handler(job_descs: list[tuple], batch_size) -> tuple[list, list, list]:
    # Collect every chunk with metadata
    # Run NER once across all chunks
    # Map results back to ids and section types
    pass

