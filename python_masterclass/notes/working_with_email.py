import smtplib
import getpass


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

#Call this immediately Next
smtp_object.ehlo()
#Call this immediately Next

# intiate encryption
smtp_object.starttls()

email = getpass.getpass('E-mail Please:')
pss = getpass.getpass('Password please:* ')

smtp_object.login(email, pss)

from_address = email
to_address = email
subject = input('enter subject: ')
message = input('enter body: ')

msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()