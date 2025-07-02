

import imaplib
import email
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging

# --- Configurations ---
EMAIL_HOST = 'imap.gmail.com'
EMAIL_PORT = 993
EMAIL_USER = 'your_email@gmail.com'
EMAIL_PASS = 'your_app_password'
VIRUSTOTAL_API_KEY = 'your_virustotal_api_key'
LOG_FILE = 'phishing_logs.txt'

# --- Setup Logging ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# --- Utility Functions ---
def extract_urls_from_email(msg):
    urls = set()
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/html':
                html = part.get_payload(decode=True).decode(errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                for link in soup.find_all('a', href=True):
                    urls.add(link['href'])
    return list(urls)

def is_url_suspicious(url):
    parsed = urlparse(url)
    if not parsed.scheme.startswith("http"):
        return False
    if len(parsed.netloc.split('.')) < 2:
        return True
    if any(keyword in url.lower() for keyword in ['login', 'verify', 'update', 'secure']):
        return True
    return False

def check_virustotal(url):
    headers = {'x-apikey': VIRUSTOTAL_API_KEY}
    response = requests.post("https://www.virustotal.com/api/v3/urls", 
                             headers=headers, 
                             data={"url": url})
    if response.status_code == 200:
        url_id = response.json()['data']['id']
        report = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
        if report.status_code == 200:
            verdict = report.json()['data']['attributes']['last_analysis_stats']
            if verdict['malicious'] > 0 or verdict['suspicious'] > 0:
                return True
    return False

# --- Email Scanner ---
def scan_emails():
    mail = imaplib.IMAP4_SSL(EMAIL_HOST, EMAIL_PORT)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")

    _, message_nums = mail.search(None, 'ALL')
    for num in message_nums[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        subject = msg.get("Subject", "(No Subject)")
        sender = msg.get("From", "Unknown")
        urls = extract_urls_from_email(msg)

        for url in urls:
            if is_url_suspicious(url):
                try:
                    if check_virustotal(url):
                        log = f"Phishing detected! Subject: {subject}, From: {sender}, URL: {url}"
                        print(log)
                        logging.warning(log)
                except Exception as e:
                    logging.error(f"Error checking URL {url}: {str(e)}")

    mail.logout()

if __name__ == "__main__":
    print("🚨 Starting Phishing Email Deactivation Tool...")
    scan_emails()
    print("✅ Scan complete. Check logs for details.")
