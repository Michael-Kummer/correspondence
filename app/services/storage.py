from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import json
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
vm_ip = os.environ["GARAGE_IP_PORT"]
key_id = os.environ["GARAGE_API_KEY_ID"]
api_key = os.environ["GARAGE_API_KEY"]
bucket_name = os.environ["BUCKET_NAME"]

client = Minio(vm_ip,
        access_key=key_id,
        secret_key=api_key,
        region="garage",
        secure=False
        )

def fetch_files(basefilepath: str=""):
    logging.info('fetching files')
    fetched_files = client.list_objects(bucket_name, prefix=basefilepath)
    logging.debug(f'files fetched: {fetched_files}')
    objects = list(map(vars, fetched_files))

    return json.dumps(objects, default=str)

def placefile(filepath):

    return

def main():
    fetch_files()
    return

if __name__ == "__main__":
    main()
