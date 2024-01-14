import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from tqdm import tqdm

emails = []
with open('emails.txt', 'r') as f:
    for line in f.readlines():
        # Assuming each line contains a single email address
        email = line.strip()  # Remove leading/trailing whitespaces
        emails.append(email)


for email in tqdm(emails):  
   
    # Define to/from
    sender = 'youremail@website.com'
    sender_title = "your name"
    recipient = email
    
    # Create message
    msg = MIMEText("Message text", 'plain', 'utf-8')
    msg['Subject'] =  Header("subject", 'utf-8')
    msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
    msg['To'] = recipient
    
    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.website.com', 465)
    
    # Perform operations via server
    server.login('your username', 'your password')
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()

