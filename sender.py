import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import random
import socks
import os
import socket
import time
import argparse
from threading import Thread

smtp_servers = [
    {'server': 'smtp.server.com', 'port': 465, 'email': 'email@server.com', 'password': 'passwd'}
]

def load_proxies_from_file(proxy_file):
    proxies = []
    if os.path.exists(proxy_file):
        with open(proxy_file, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    proxies.append({
                        'host': parts[0],
                        'port': int(parts[1]),
                        'username': parts[2] if parts[2] != '' else None,
                        'password': parts[3] if parts[3] != '' else None
                    })
    return proxies

def set_socks5_proxy(proxy_info):
    socks.setdefaultproxy(
        socks.PROXY_TYPE_SOCKS5,
        proxy_info['host'],
        proxy_info['port'],
        True if proxy_info['username'] else False,
        proxy_info['username'],
        proxy_info['password']
    )
    socket.socket = socks.socksocket

def send_email(to_email, subject, html_message, fake_as_email, fake_as_name, proxy=None):
    msg = MIMEMultipart()
    msg['From'] = f"\"{fake_as_name}\" <{fake_as_email}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg['X-Priority'] = '1'
    msg['X-MSMail-Priority'] = 'High'
    msg['Importance'] = 'High'
    msg.attach(MIMEText(html_message, 'html'))
    if proxy:
        print(f"Utilizzo proxy: {proxy['host']}:{proxy['port']}")
        set_socks5_proxy(proxy)
    try:
        data = random.choice(smtp_servers)
        server = smtplib.SMTP(data["server"], data["port"])
        server.starttls()
        server.login(data["email"], data["password"])
        server.sendmail(data["email"], to_email, msg.as_string())
        server.quit()
        print(f"Email inviata con successo a: {to_email}")
    except Exception as e:
        print(f"Errore durante l'invio dell'email a: {to_email}. Errore: {str(e)}, riprovo")
        Thread(target=send_email, args=(to_email, subject, html_message, fake_as_email, fake_as_name, proxy)).start()

def send_mass_email(email_list_file, html_template_file, subject, fake_as_email, fake_as_name, proxy_file=None):
    proxies = load_proxies_from_file(proxy_file) if proxy_file else []
    use_proxy = True if proxies else False
    with open(email_list_file, 'r') as file:
        email_list = file.readlines()
    email_list = [email.strip() for email in email_list]
    with open(html_template_file, 'r', encoding='utf-8') as file:
        html_message = file.read()
    for to_email in email_list:
        proxy = random.choice(proxies) if use_proxy else None
        Thread(target=send_email, args=(to_email, subject, html_message, fake_as_email, fake_as_name, proxy)).start()
        time.sleep(random.uniform(2, 5))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phishing Email Sender Script with optional SOCKS5 proxy support')
    parser.add_argument('--email_list', required=True, help='Path to the file containing email list')
    parser.add_argument('--html_template', required=True, help='Path to the HTML email template file')
    parser.add_argument('--subject', required=True, help='Subject of the email')
    parser.add_argument('--fake_email', required=True, help='Email address to spoof as sender')
    parser.add_argument('--fake_name', required=True, help='Name to show as sender')
    parser.add_argument('--proxy_file', required=False, help='Path to the file containing SOCKS5 proxies')
    args = parser.parse_args()
    send_mass_email(args.email_list, args.html_template, args.subject, args.fake_email, args.fake_name)
