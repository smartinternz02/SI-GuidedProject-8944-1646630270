# Library to have connection to your gmail
import smtplib
import nltk
nltk.download('stopwords')
# library to extract the entities form your resume
from pyresparser import ResumeParser
import nltk
nltk.download('stopwords')
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security
s.starttls() 

# Authentication 
s.login("bharatakhil1122@hmail.com", "akhil@1122") 

# give a subject   
SUBJECT = "Interview Call"

# skills requirement for Ai developer
python_skills = ["ml","ai","matplotlib","seabon",
                 "python","reression","algorithms", 
                 "Pandas","data analysis","keras",
                 "tensorflow","artificial intelligence",
                 "data visualization","opencv"]
# skills requirement for Java developer
java_skills  = []

# extract the skills from resume
data = ResumeParser('Resume.pdf').get_extracted_data()
print(data)
# grab the name
name = data['name']
# grab the Email
email = data['email']
# grab the Skills
skills = data["skills"]
# lowercase the skills
actual_skills = [i.lower() for i in skills ]

  
# using list comprehension 
# checking if string contains list element 
Skills_matched = [ele for ele in actual_skills 
                if(ele in python_skills)] 



# check the number of skills matched
if(len(Skills_matched) >= 4 ):
    
    print("he is eligible")
    # create a text that is to sent in an email
    TEXT = "Hello " + name + ",\n\nThanks for applying to the job post-AI/ML Developer. " \
                                     "Your skill matches our requirements. " \
                                     "Kindly, let us know your available time for initial round of interview." \
                                     "\n\nThanks and Regards,\n\nTalent acquisition team | SmartBridge" 
    # send mail
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #send the mail
    s.sendmail("bharatakhil1122@gmail.com", email, message) 
    #quit the session
    s.quit()    
else:
    print("sorry we cant process your candidature")
    
    TEXT = "Hello " + name + ",\n\nThanks for applying to the job post-AI/ML Developer. " \
                                     "Your candidature is rejected." \
                                     "\n\nThanks and Regards,\n\nTalent acquisition team | SmartBridge"   
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("bharatakhil1122@gmail.com", email, message) 
    s.quit() 
    