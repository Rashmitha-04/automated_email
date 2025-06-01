from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
import os
import smtplib
from email.message import EmailMessage
import mimetypes

def send_email_with_attachment():
    # Get credentials from environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = "receiver@example.com"  # Change to your recipient
    subject = "Test Email with Attachment"
    body = "Hello, this is a test email sent from Python with an attachment."
    attachment_path = "sample.pdf"

    # Create email message
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach the file
    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        if mime_type is None:
            mime_type = "application/octet-stream"
        maintype, subtype = mime_type.split("/", 1)
        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)
    else:
        print(f"Attachment file '{attachment_path}' not found.")
        return

    # Send email via Gmail SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
if __name__ == "__main__":
    send_email_with_attachment()
