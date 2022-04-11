from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import smtplib
from pyresparser import ResumeParser
import nltk
nltk.download('stopwords')
# creates SMTP session
    
s = smtplib.SMTP('smtp.gmail.com', 465) 
s.starttls() 

SUBJECT = "Interview Call"

python_skills = ["ml","ai","matplotlib","seabon",
                 "python","reression","algorithms",
                 "Pandas","data analysis","keras",
                 "tensorflow","artificial intelligence",
                 "data visualization","opencv"]

java_skills  = []


app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('index.html')
@app.route('/apply_job')
def applyjob():
    return render_template("apply_job.html")


@app.route('/fill_form')
def fillform():
    return render_template("form.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        data = ResumeParser(f.filename).get_extracted_data()
        name = data['name']
        email = data['email']
        skills = data["skills"]
        actual_skills = [i.lower() for i in skills ]
        # using list comprehension
        # checking if string contains list element
        Skills_matched = [ele for ele in actual_skills if(ele in python_skills)]
        if(len(Skills_matched) >= 4 ):
            print("he is eligible")
            s.login("bharatakhil1122@gmail.com", "akhil@1122")
            TEXT = "Hello " + name + ",\n\nThanks for applying to the job post-AI/ML Developer. " \
                                             "Your skill matches our requirements. " \
                                             "Kindly, let us know your availabl for initial round of interview." \
                                             "\n\nThanks and Regards,\n\nTalent acquisition team | SmartBridge" 
            message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail("bharatakhil1122@gmail.com", email, message)
            s.quit()
            return render_template('form.html',prediction = 
                                   """Thanks  for applying youwill be mailed about
                                   your candidature""")

        else:
            print("sorry we cant process your candidature")
            s.login("bharatakhil1122@gmail.com", "akhil@1122")
            TEXT = "Hello " + name + ",\n\nThanks for applying to the job post-AI/ML Developer. " \
                                            "Your candidature is rejected." \
                                            "\n\nThanks and Regards,\n\nTalent acquisition team | SmartBridge" 
            message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail("bharatakhil1122@gmail.com", email, message)
            s.quit()
            return render_template('form.html',prediction = 
                                   """Thanks  for applying youwill be 
                                   mailed about your candidature""")
    else:
        return render_template('index.html')
		
if __name__ == '__main__':
   app.run(debug=False)
   
   
   
   
   
   
   
   
   