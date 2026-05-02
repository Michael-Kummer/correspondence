from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
vm_ip = os.environ["GARAGE_IP_PORT"]
key_id = os.environ["GARAGE_API_KEY_ID"]
api_key = os.environ["GARAGE_API_KEY"]

logger = logging.getLogger(__name__)

def clean():

    return

def file_upload(filename):
    client = Minio(vm_ip,
    access_key=key_id,
    secret_key=api_key,
    region="garage",
    secure=False,
    )

    source_file = "test.txt"
    bucket_name="text-images"
    destination_file="test-upload.txt"

    client.fput_object(
            bucket_name,
            destination_file,
            source_file,
            )


    return

def main():
    client = Minio(vm_ip,
    access_key=key_id,
    secret_key=api_key,
    region="garage",
    secure=False,
    )

    print(client.list_buckets())

    source_file = "test.txt"
    bucket_name="text-images"
    destination_file="test-upload.txt"

    client.fput_object(
            bucket_name,
            destination_file,
            source_file,
            )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occured.", exc)
