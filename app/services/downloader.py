from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import datetime
import time
import os
import sys
import csv
import logging

"""
Downloader script for my correspondence project. 
Interacts with publically available API's
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
DEBUG = True
#DEBUG = False

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", timestamp, "images")
LOG_FILE = os.path.join(BASE_DIR, "outputs", timestamp, "post_log.csv")

load_dotenv(os.path.join(BASE_DIR, ".env"))

REDDIT = {
    "subreddit_posts": "https://www.reddit.com/r/{subreddit}/{sort}.json?limit=100",
    "search": "https://www.reddit.com/r/{subreddit}/search.json?q={query}&restrict_sr=on&type=link",
    "target_subreddits": [s.strip() for s in os.environ["TARGET_SUBREDDITS"].split(",") if s.strip()],
}

headers = {"User-Agent": "correspondence/1.0"}

def load_seen():
    """
    Loads seen csv and passes through a set of all the seen links
    INPUT: NONE
    OUTPUT: seen (set)
    """

    seen = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                seen.add(row["id"])
    return seen


def log_post(item, filename):
    """
    Loads seen csv and passes through a set of all the seen links
    INPUT: item, filename (our jpeg that we downloaded)
    OUTPUT: NONE
    """
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "subreddit", "url", "filename", "date"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "id": item["id"],
            "subreddit": item["sub"],
            "url": item["url"],
            "filename": filename,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

def fetchurls(sort="new"):
    """
    Fetches i.imgur.com and i.redd.it from subreddits
    """
    pages = 10 if sort == "top" else 1
    urls = []
    for sub in REDDIT["target_subreddits"]:
        after = None
        for page in range(pages):
            url = REDDIT["subreddit_posts"].format(subreddit=sub, sort=sort)
            if sort == "top":
                url += "&t=all"
            if after:
                url += f"&after={after}"

            response = requests.get(url, headers=headers)
            data = response.json()
    
            for post in data["data"]["children"]:
                urls.extend(extract_image_urls(post))

            after = data["data"].get("after")
            if not after:
                break
            if not DEBUG:
                time.sleep(6)
    return urls

def extract_image_urls(post):
    urls = []
    data = post["data"]
    url = data.get("url", "")
    sub = data.get("subreddit", "unknown")
    post_id = data.get("id", "unknown")

    if "i.redd.it" in url or "i.imgur.com" in url:
        urls.append({"url": url, "sub": sub, "id": post_id})

    elif "gallery" in url and "media_metadata" in data:
        for i, item in enumerate(data["media_metadata"].values()):
            if item.get("status") == "valid" and "s" in item:
                img_url = item["s"].get("u", "").replace("&amp;", "&")
                if img_url:
                    urls.append({"url":img_url, "sub":sub, "id": f"{post_id}_{i}"})

    elif "imgur.com" in url and "i.imgur" not in url and "/a/" not in url:
        urls.append({"url": url + ".jpg", "sub": sub, "id": post_id})

    return urls

def download_images(image_list, output_dir=OUTPUT_DIR):
    os.makedirs(output_dir, exist_ok=True)
    seen = load_seen()
    new_count = 0

    for item in image_list:
        if item["id"] in seen:
            continue
        response = requests.get(item["url"], headers=headers)
        if response.status_code == 200:
            ext = os.path.splitext(urlparse(item["url"]).path)[1] or ".jpg"
            filename = f"{item['sub']}_{item['id']}{ext}"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            log_post(item, filename)
            seen.add(item["id"])
            new_count += 1

    if not DEBUG:
        time.sleep(0.25)
    return

def main(mode: str = "new"):
    urls = fetchurls(sort=mode)
    download_images(urls)
    return

if __name__=="__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "new"
    main(mode)
