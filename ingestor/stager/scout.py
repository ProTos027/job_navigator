async def _fetch(company, client, max_retries= 3):
    
    # extract company details
    # construct URL
    # implement retry logic
            # make request and get response
            # parse jobs from response
            # enrich jobs with company details
    # handle exceptions and implement backoff    
    pass

async def producer(companies, queue):
    # define semaphore to limit concurrent requests
    # use a single shared HTTP client for  requests
        # run async tasks for all companies
    # signal finish to consumer
    pass
    
async def consumer(q):
    # wait for job to enter the queue
    # if no more jobs, flush and exit
    # manage concurrency
    # push results to global list
    pass
async def _run_pipeline(companies, q):
    # define producer and consumer tasks
    # assign tasks asynchronously
    pass

def scout() -> list[dict]:
    
    # connect to DB and fetch companies details
            # create table if not exists
    # define async queue
    # start async run
    pass
