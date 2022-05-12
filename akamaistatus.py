import subprocess
import smtplib
import email.utils

def send_email_down(send_from, send_to):
    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "Alert - Akamai CEF Connector Offline!"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("Warning! The Akamai CEF Connector is down!")
    server = smtplib.SMTP(host="smtphost", port=#)
    server.login("user", "password")
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()

def send_email_up(send_from, send_to):
    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "Notice - Akamai CEF Connector Online!"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("Notice - The Akamai CEF Connector is running.")
    server = smtplib.SMTP(host="smtphost", port=#)
    server.login("user", "password")
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()

def send_email_error(send_from, send_to):
    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "Error! Akamai CEF Connector Status Unknown!"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("Error! - Unable to determine health of the Akamai CEF Connector!")
    server = smtplib.SMTP(host="smtphost", port=#)
    server.login("user", "password")
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()


    status = subprocess.getoutput(["sudo /path/to/install/AkamaiCEFConnector.sh status"])

if "is running" in status:
    send_email_up("sender", "receiver")
elif "is not running" in status:
    send_email_down("sender", "receiver")
else:
    send_email_error("sender", "receiver")
