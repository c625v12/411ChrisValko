import smtplib

from email.mime.text import MIMEText

fromAddress = 'cjv5110@psu.edu'
toAddress = 'cjv5110@psu.edu'
subject = 'I have to do this for a good grade'

msg = MIMEText('This too')
msg['Subject'] = subject
msg['From'] = fromAddress
msg['To'] = toAddress

try :
	s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
	s.sendmail(fromAddress, [toAddress], msg.as_string())
except Exception as e:
	print ("Error %s" % e.args[0])
finally:
	s.quit()
