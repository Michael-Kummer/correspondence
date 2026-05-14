from dotenv import load_dotenv
from ollama import chat
from ollama import Client
from ollama import ChatResponse
import json_repair
import os
import json

MODEL_NAME = "gemma4:e4b"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
API_IP = os.environ["OLLAMA_HOST"]
PROMPT_DIR = os.path.join(BASE_DIR, "prompt.txt")
IMAGE_DIR = os.path.join(BASE_DIR, "outputs/examples/texts_1cjys01.png")


client = Client(host=f'http://{API_IP}')

def main():
    print(BASE_DIR)
    print(IMAGE_DIR)
    with open(PROMPT_DIR) as f:
        prompt = f.read()

    response = client.chat(
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": prompt, "images": [IMAGE_DIR]}],
    )

    repaired = json_repair.loads(response)
    print(repaired)

    return


if __name__ == "__main__":
    main()
