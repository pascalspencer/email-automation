# Email Automation using Python

This script automates the process of sending emails using Python's `smtplib` and `email` modules. It loads email credentials from an `.env` file for security and sends an email via Gmail's SMTP server.

## Features
- Sends automated emails using SMTP
- Uses environment variables for credentials security
- Supports TLS encryption for secure email transmission

## Requirements
Ensure you have Python installed and install the required dependencies:
```sh
pip install python-dotenv
```

## Setup
1. Create a `.env` file in the project directory with the following variables:
    ```env
    SENDER=your-email@gmail.com
    RECEIVER=recipient-email@gmail.com
    PASSWORD=your-email-password
    ```
2. Clone the repository:
    ```sh
    git clone https://github.com/your-username/email-automation.git
    cd email-automation
    ```
3. Install the required package:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the script using:
```sh
python Email_program.py
```

## Security Note
- Do not share your `.env` file or credentials publicly.
- Consider using an app-specific password instead of your main email password.
- Enable "Less secure app access" if needed or use OAuth authentication for better security.



