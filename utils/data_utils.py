import requests
from pathlib import Path

def load_simplewiki_data():
    # Replace this with the actual URL you copy from the dumps website
    URL = "https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pages-articles.xml.bz2"

    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_path = raw_dir / "simplewiki.xml.bz2"

    print(f"Downloading to {out_path} from {URL} ...")
    resp = requests.get(URL, stream=True)
    resp.raise_for_status()

    with open(out_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1 << 20):  # 1 MB
            if chunk:
                f.write(chunk)

    print("Done.")

if __name__ == "__main__":
    load_simplewiki_data()