# IT

---

# PhishMaster - Script di invio email per il Red Teaming

## Descrizione

PhishMaster è uno script Python progettato per inviare email di phishing in massa, utilizzando server SMTP casuali e supporto opzionale per proxy SOCKS5. È pensato per simulazioni di Red Teaming, con l'obiettivo di testare le difese contro attacchi di phishing. **Si raccomanda di utilizzarlo solo per scopi etici e legali**, con il consenso del destinatario.

## Caratteristiche
- Invio di email con spoofing del mittente (nome ed email falsi).
- Utilizzo di server SMTP casuali.
- Supporto per l'uso di proxy SOCKS5.
- Invio email in massa con HTML personalizzabile.
- Riprova automatica in caso di errore di invio.
- Possibilità di inviare email con priorità alta.

## Requisiti
- Python 3.x
- Moduli Python: `smtplib`, `email`, `socks`, `argparse`, `threading`

## Installazione
1. Clona la repository GitHub:
   ```bash
   git clone https://github.com/Vit8816/PhishMaster
   cd PhishMaster
   ```
2. Installa i moduli richiesti:
   ```bash
   pip install pysocks
   ```

## Utilizzo
1. Prepara un file con la lista di email, un template HTML per il corpo del messaggio e, opzionalmente, un file con proxy SOCKS5.
2. Esegui lo script con i seguenti parametri:
   ```bash
   python sender.py --email_list <email_list.txt> --html_template <template.html> --subject "Oggetto Email" --fake_email "falso@esempio.com" --fake_name "Nome Falso" [--proxy_file proxy.txt]
   ```

   - `--email_list`: File contenente una lista di email, una per riga.
   - `--html_template`: File HTML per il corpo del messaggio.
   - `--subject`: Oggetto dell'email.
   - `--fake_email`: Email da mostrare come mittente.
   - `--fake_name`: Nome da mostrare come mittente.
   - `--proxy_file`: (Opzionale) File contenente i proxy SOCKS5.

## Avvertenze
- **Non usare questo script per attacchi non autorizzati o illegali.**
- Si consiglia l'uso solo in ambienti controllati e con autorizzazione.

---

# EN

---

# PhishMaster - Email Sending Script for Red Teaming

## Description

PhishMaster is a Python script designed to send mass phishing emails using random SMTP servers and optional SOCKS5 proxy support. It is intended for Red Teaming simulations, with the goal of testing defenses against phishing attacks. **It is recommended to use this tool only for ethical and legal purposes**, with the recipient's consent.

## Features
- Send emails with spoofed sender information (fake name and email).
- Randomized SMTP server usage.
- SOCKS5 proxy support.
- Mass email sending with customizable HTML templates.
- Automatic retry in case of email delivery failure.
- Ability to send emails with high priority.

## Requirements
- Python 3.x
- Python modules: `smtplib`, `email`, `socks`, `argparse`, `threading`

## Installation
1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/Vit8816/PhishMaster
   cd PhishMaster
   ```
2. Install the required modules:
   ```bash
   pip install pysocks
   ```

## Usage
1. Prepare a file containing the list of email addresses, an HTML template for the message body, and optionally, a file with SOCKS5 proxies.
2. Run the script with the following parameters:
   ```bash
   python sender.py --email_list <email_list.txt> --html_template <template.html> --subject "Email Subject" --fake_email "fake@example.com" --fake_name "Fake Name" [--proxy_file proxy.txt]
   ```

   - `--email_list`: File containing a list of email addresses, one per line.
   - `--html_template`: HTML file for the email body.
   - `--subject`: Subject of the email.
   - `--fake_email`: Email address to spoof as the sender.
   - `--fake_name`: Name to display as the sender.
   - `--proxy_file`: (Optional) File containing SOCKS5 proxies.

## Warnings
- **Do not use this script for unauthorized or illegal activities.**
- It is recommended to use this only in controlled environments and with proper authorization.
