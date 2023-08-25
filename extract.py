"""
python function that extract pdf file from a given url
"""
import requests
import os

def download_pdf(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {save_path} successfully.")
    else:
        print(f"Failed to download {save_path}.")

if __name__ == '__main__':
    pdf_url =''
    save_path = os.path.join(os.getcwd(), 'test.pdf')
    download_pdf(pdf_url, save_path)