import subprocess

def etl():
    subprocess.run(["python", "-m", "ingestor.stager.stager"], check=True)
    subprocess.run(["python", "-m", "ingestor.transformer.transformer"], check=True)
    subprocess.run(["python", "-m", "ingestor.clusterer.clusterer"], check=True)

etl()


