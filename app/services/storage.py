from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import json
import os
import logging
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
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

def fetch_files(fileprefix: str=""):
    logging.info('fetching files')
    fetched_files = client.list_objects(bucket_name, prefix=fileprefix)
    logging.debug(f'files fetched: {fetched_files}')
    objects = list(map(vars, fetched_files))

    return json.dumps(objects, default=str)

def place_file(filename: str = timestamp):
    filedir = os.path.join(BASE_DIR, "outputs")
    logging.debug(f'{filename}')
    csv_filepath = os.path.join(filedir, filename, "post_log.csv")
    images_filepath = os.path.join(filedir, filename, "images")

    logging.info('placing file')
    logging.debug(f"file directory: {filedir}")

    #Uploading csv
    object_filename = os.path.join(timestamp, "post_log.csv")
    result = client.fput_object(bucket_name, 
                                object_name=object_filename,
                                file_path=csv_filepath)

    #Upload images in folder
    for filename in os.listdir(images_filepath):
        try:
            object_filename = os.path.join(timestamp, filename)
            filepath = os.path.join(images_filepath, filename)
            result = client.fput_object(bucket_name, 
                                        object_name=object_filename,
                                        file_path=filepath)
            logging.debug(f"Uploaded successfully. ETag: {result.etag}")
        except FileNotFoundError:
            logging.warning("Local file doesn't exist")
        except S3Error as e:
            logging.error(f"MinIO/S3 error: {e.code} - {e.message}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
    
    return True

def main():
    #fetch_files()
    return

if __name__ == "__main__":
    main()
