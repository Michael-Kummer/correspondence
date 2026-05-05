# Correspondence
A handbuilt chess themed OCR based pipeline I created to rank conversations online and assign ELO to participants. This was built so I can familiarize myself with the stack and I think trying to identify language appropriateness is a fun side project.
The code is free to be used elsewhere. It requires a local ollama instance for converting images to text, a local Postgresdb for storing said text, and a local/cloud object storage for storing raw images of texts.

ELO and texting performance:
The training set was ranked by me. I created a platform to let me easily do the rankings for our train test split.

Stack:
- FastAPI
- Docker 
- Postgres
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

### Object Storage CLI Expamples
```Bash

# list buckets
aws s3 ls

# list objects of a bucket
aws s3 ls s3://text-image

# copy from your filesystem to garage
aws s3 cp /proc/cpuinfo s3://nextcloud-bucket/cpuinfo.txt

# copy from garage to your filesystem
aws s3 cp s3://nextcloud-bucket/cpuinfo.txt /tmp/cpuinfo.txt

```


