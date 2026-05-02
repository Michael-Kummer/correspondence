# Correspondence
A handbuilt chess themed OCR based pipeline I created to analyze conversations that I host on my homeserver. This was built so I can familiarize myself with the stack and I think trying to identify LLM language appropriateness is a fun side project.
The code can be used, but it requires a local ollama instance for analyzing and a local/cloud object storage.

Stack:
- FastAPI
- Docker 
- Garage (Object Storage)
- Ollama (Hosts LightOnOCR-2)

### Usage
#### Scrape new subreddits
```Bash
curl -X POST localhost:8000/scrape-new
```

#### Get files
```Bash
curl localhost:8000/storage/get-files

```

#### Upload to S3 todays scrapes
```Bash
curl -X POST http://localhost:8000/storage/upload-today
```

#### Upload to S3 scrapes from a dfiferent day
```Bash
curl -X POST http://localhost:8000/storage/upload-today
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


