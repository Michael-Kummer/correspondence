# Correspondence
A chess themed OCR based pipeline to analyze images of texts that I have on my home server.
The code can be used, but it requires a local ollama instance for analyzing and a local/cloud object storage. 

Stack:
- FastAPI
- Docker 
- Garage (Object Storage)
- Ollama (Hosts LightOnOCR-2)

### Usage

```Bash
curl -X POST localhost:8000/scrape-new
```

downloader.py
Downloads all the images to an images folder

```Python
python3 downloader.py top
```

### Object Storage CLI usage
```Bash

# list buckets
aws s3 ls

# list objects of a bucket
aws s3 ls s3://nextcloud-bucket

# copy from your filesystem to garage
aws s3 cp /proc/cpuinfo s3://nextcloud-bucket/cpuinfo.txt

# copy from garage to your filesystem
aws s3 cp s3://nextcloud-bucket/cpuinfo.txt /tmp/cpuinfo.txt

```


