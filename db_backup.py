#!/usr/bin/env python3
import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import logging

load_dotenv()

def send_email_notification(from_email, to_email, subject, body, csv_data=None, cc=None):
    try:
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))
        smtp_username = os.getenv('SMTP_USERNAME')
        smtp_password = os.getenv('SMTP_PASSWORD')

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        # Add CC recipients if provided
        if cc:
            msg['Cc'] = ', '.join(cc)
            to_email += cc

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_email, msg.as_string())

        logging.info('Email sent successfully!')
    except Exception as e:
        loggin.error(f'Error sending email: {e}')
        raise e

def backup_mysql():
    try:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        backup_filename = f"backup_file_{current_datetime}.sql"

        os.system(f"mysqldump -u israel -p deployguru > {backup_filename}")

        # Send email notification for success
        send_email_notification(
            from_email=os.getenv('SMTP_USERNAME'),
            to_email=["israel7payment@gmail.com"],
            subject="MySQL Backup Success",
            body=f"Backup file {backup_filename} created successfully."
        )

    except Exception as e:
        # Send email notification for error
        send_email_notification(
            from_email=os.getenv('SMTP_USERNAME'),
            to_email=["israel7payment@gmail.com"],
            subject="MySQL Backup Error",
            body=f"An error occurred while creating MySQL backup: {str(e)}"
        )
        raise e

def main():
    # Backup MySQL database
    backup_mysql()

if __name__ == "__main__":
    main()
