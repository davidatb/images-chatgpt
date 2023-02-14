    # -*- coding: windows-1252 -*-
import openai
import requests
import json
from requests.structures import CaseInsensitiveDict


# openai.api_key = "MY_API_KEY"
with open("config.json") as f:
    config = json.load(f)
api_key = config["openai"]["api_key"]
openai.api_key = api_key

model_engine = "image-alpha-001"
model_prompt = input("Se especifico para generar imágenes de mejor calidad: ")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {openai.api_key}"

data = """
{
    """
data += f'"model": "{model_engine}",'
data += f'"prompt": "{model_prompt}",'
data += """
    "num_images":4,
    "size":"1024x1024",
    "response_format":"url"
}
"""

resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data)

if resp.status_code != 200:
    raise ValueError("Failed to generate image "+resp.text)

response_text = resp.text
response_json = json.loads(response_text)
image_url = response_json['data'][0]['url']
print(image_url)
