import requests
import os

API_BASE = "http://127.0.0.1:8000/api"

def upload_file(path: str):
    url = f"{API_BASE}/upload/"
    with open(path, "rb") as f:
        files = {"file": (os.path.basename(path), f, "text/csv")}
        r = requests.post(url, files=files)
    r.raise_for_status()
    return r.json()

def get_history():
    url = f"{API_BASE}/history/"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def download_report(dataset_id: int, save_path: str):
    url = f"{API_BASE}/report/{dataset_id}/"
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(save_path, "wb") as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)
