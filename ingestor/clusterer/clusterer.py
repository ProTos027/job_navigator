from ingestor.clusterer.embedder import embed
from ingestor.clusterer.picker import entity_gen
from ingestor.clusterer.computer import compute_cluster
from ingestor.clusterer.loader import insert_clust, update_cluster_lookup, refresh_lookup

col= entity_gen()

def cluster():
    
    # refresh cluster lookup table
    print("Refreshing cluster lookup table...")
    refresh_lookup()
    print("Refreshed cluster lookup table.")
    
    while True:
        
        # get columns
        print("Fetching column...")
        val= None
        if val is None:
            print("No more columns to process. Exiting.")
            break
        col_name, cur_col= None, None
        print(f"Fetched column: abc")
        
        # compute embeddings
        print("Computing embeddings...")
        embeddings= embed(cur_col)
        print("Computed embeddings.")
        
        # compute clusters
        print("Computing clusters...")
        clust= compute_cluster(cur_col, embeddings)
        cor_cluster= clust['item_cluster']
        lookup= clust['cluster_lookup_data']
        print("Computed clusters.")
        
        # upsert cluster lookup and insert clusters
        print("Updating cluster lookup and inserting clusters...")
        update_cluster_lookup(col_name, lookup)
        insert_clust(col_name[0], cor_cluster)
        print(f"Updated and inserted for abc.")
        
cluster()

