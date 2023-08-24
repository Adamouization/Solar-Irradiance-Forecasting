import requests

from tqdm.contrib import tzip


# Constants
ACCESS_TOKEN = "xvB2DVOuPlGovuFhzGyLYrjvyWe8TpoTco7VS5lXjjd6xVMw8RJcY5rpsdOR"
RECORD_ID = "2826939"
IS_SKIP_BZ2 = False
IS_ONLY_BZ2 = True


# Get all files in Zenodo record to download
r = requests.get(f"https://zenodo.org/api/records/{RECORD_ID}", params={'access_token': ACCESS_TOKEN})
download_urls = [f['links']['self'] for f in r.json()['files']]
filenames = [f['key'] for f in r.json()['files']]

print(r.status_code)
print(download_urls)
print(filenames)


def download_file(filename):
    """
    Download and save a file.
    """
    r = requests.get(url, params={'access_token': ACCESS_TOKEN})
    with open(filename, 'wb') as f:
        f.write(r.content)


# Loop through all files to download
for filename, url in tzip(filenames, download_urls):
    # Don't download images (only csv and py)
    if IS_SKIP_BZ2 and not IS_ONLY_BZ2:
        if ".csv" in filename or ".py" in filename:
            print(f"Downloading: {filename}...")
            download_file(filename)
        else:
            print(f"Skipping: {filename}.")
    
    # Download only zipped images
    if IS_ONLY_BZ2 and not IS_SKIP_BZ2:
        if ".bz2" in filename:
            print(f"Downloading: {filename}...")
            download_file(filename)
        else:
            print(f"Skipping: {filename}.")
    
    # Download everything, including images
    if not IS_ONLY_BZ2 and not IS_ONLY_BZ2:
        print(f"Downloading: {filename}...")
        download_file(filename)
