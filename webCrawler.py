# This python program can help to crawl the web site content.
# Here just replace the url "example.com" with target url.
# Opensource <3.

import requests

url = "example.com"
get_response = requests.get("http://"url)
print (get_response)

def download(url):
    get_response = requests.get(url)
    file_name=url.sploit("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)

download(url)