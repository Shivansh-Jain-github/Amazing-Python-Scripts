# Automatic WhatsApp Message Sender

This repository provides a Python script that uses the `pywhatkit` library to send WhatsApp messages automatically at a specified time. The script allows you to schedule a message to be sent to a recipient using WhatsApp Web.

## Prerequisites

- Python 3.x
- Install the `pywhatkit` library using the following command:

  ```bash
  pip install pywhatkit
  ```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/whatsapp-auto-message.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd whatsapp-auto-message
   ```

3. Replace `'YOUR_PHONE_NUMBER'` with the recipient's phone number in international format (including the country code) and adjust the `send_time_hour` and `send_time_minute` variables in the `send_message.py` file.

4. Run the script using your Python interpreter:

   ```bash
   python send_message.py
   ```

## Usage

The `send_message.py` script in this repository demonstrates how to use the `pywhatkit` library to send a WhatsApp message automatically at a specified time. It performs the following steps:

1. Calculates the delay until the specified sending time.
2. Waits until the specified time is reached.
3. Sends the specified message to the specified recipient using WhatsApp Web.

## Important Note

- Make sure you have WhatsApp Web logged in on your browser when running the script.
- The script may not work properly if your computer goes to sleep or if there are issues with the internet connection.
- Use this script responsibly and only for legitimate and non-spam purposes.

## Example Output

```
Waiting for 32400.0 seconds until 12:30
Message sent successfully!
```

## Customize

You can customize the recipient's phone number, message content, and sending time in the `send_message.py` file according to your requirements.

Explore the capabilities of the `pywhatkit` library and have fun experimenting with automatic WhatsApp messaging!

