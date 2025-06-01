# Automated Email Sender with Attachment 

A simple Python script to send automated emails with attachments using Gmail SMTP and environment variables for secure credentials.

# Features 

-Send emails with attachments (PDF, images, etc.)
-Uses Gmail SMTP with SSL for secure connection
-Credentials loaded securely from `.env` file
-Easy to customize recipient, subject, and message

## Setup

1. Enable 2-Step Verification on your Google Account.
2. Generate an App Password at: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create a `.env` file in the project folder with:
    SENDER_EMAIL=your_email@gmail.com
    SENDER_PASSWORD=your_app_password
4. Install dependencies:
    pip install python-dotenv
5. Place your attachment (e.g., `sample.pdf`) in the project folder.
6. Run the script:
    python week-2.py
