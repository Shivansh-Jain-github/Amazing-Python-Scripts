import pywhatkit as kit
import datetime
import time

# Set the phone number and message
phone_number = "+1234567890"  # Replace with the recipient's phone number
message = "This is an automated message."

# Set the time for sending the message (24-hour format)
send_time_hour = 12  # Replace with the desired hour
send_time_minute = 30  # Replace with the desired minute

# Calculate the delay until the specified time
current_time = datetime.datetime.now()
send_time = current_time.replace(hour=send_time_hour, minute=send_time_minute, second=0, microsecond=0)
time_difference = send_time - current_time
delay_seconds = time_difference.total_seconds()

# Wait until the specified time
print(f"Waiting for {delay_seconds} seconds until {send_time_hour:02d}:{send_time_minute:02d}")
time.sleep(delay_seconds)

# Send the message
kit.sendwhatmsg(phone_number, message, send_time_hour, send_time_minute)
print("Message sent successfully!")
