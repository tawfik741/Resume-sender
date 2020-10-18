import smtplib

import codecs

from string import Template

from email import encoders

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

import email_loader as my_loader
MY_ADDRESS = ''
PASSWORD = ''
PATH_FOR_MAIL='template.txt'
email="tboujeh@gmail.com"


#PATH_FOR_MAIL='template.txt'
#email="tboujeh@gmail.com"

def get_english():
	english=my_loader.read_english()
	return english

def get_french():
	french=my_loader.read_french()
	return french
	
def read_template(filename):
	"""
	Returns a Template object comprising the contents of the 
	file specified by filename.
	"""
	
	with codecs.open(filename, 'r', encoding='latin1' , errors='ignore' ) as template_file:
		template_file_content = template_file.read()
		
	return Template(template_file_content)


def send():
	message_template = read_template('message.txt')

	# set up the SMTP server
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	print(MY_ADDRESS)
	s.login(MY_ADDRESS, PASSWORD)

	# For each contact, send the email:
	

	#for name, email in zip(names, emails):
	#test
	contacts=get_french()
	#contacts=[]
	#contacts.append(test_contacts[0])
	
	for contact in contacts:
		msg = MIMEMultipart()       # create a message

		# add in the actual person name to the message template
		#message = message_template.substitute(PERSON_NAME=name.title())
		message = message_template.substitute(ENTERPRISE_NAME=contact["etablissement"])
		# Prints out the message body for our sake
		print(contact["etablissement"])

		# setup the parameters of the message
		msg['From']=MY_ADDRESS

		msg['To']=contact["email"]
		
		#msg['To']="tboujeh@gmail.com"
		
		first_char_for_test=contact['etablissement'][0].upper()
		if (first_char_for_test in ["A","E","O","I","U"] ):
			subject_head="Candidature pour un stage de fin d'études au sein d'"
		else :
			subject_head="Candidature pour un stage de fin d'études au sein de "
			

		msg['Subject']=subject_head+contact["etablissement"]
		
		# add in the message body
		msg.attach(MIMEText(message, 'plain'))
		
		# add in the letter file 
		
		letter_name="Lettre de motivation Emna Ben Mariem.pdf"
		
		

		letter_attachement="fghons/"+letter_name
		
		
		# Add header to variable with attachment file
		attach_letter_file=MIMEApplication(open(letter_attachement,"rb").read())
		attach_letter_file.add_header('Content-Disposition', 'attachment', filename=letter_name)
		# Then attach to message attachment file    
		msg.attach(attach_letter_file)
		
		# add in the resume file 
		resume_name="CV de Emna Ben Mariem.pdf"
		resume_attachement="fghons/"+resume_name
		
		# Add header to variable with attachment file
		attach_resume_file=MIMEApplication(open(resume_attachement,"rb").read())
		attach_resume_file.add_header('Content-Disposition', 'attachment', filename=resume_name)
		# Then attach to message attachment file    
		msg.attach(attach_resume_file)

		

		# send the message via the server set up earlier.
		s.send_message(msg)
		print ("sent")
		del msg
		
	# Terminate the SMTP session and close the connection
	s.quit()
	
if __name__ == '__main__':
	send()