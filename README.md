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
