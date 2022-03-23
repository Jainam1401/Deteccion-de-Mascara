from flask import Flask, render_template, request
import mysql.connector
import os
from flask_mail import Mail

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'projectsupervisor124@gmail.com'
app.config['MAIL_PASSWORD'] = '10162738'
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="project"
        )
        username = request.form.get('username')
        password = request.form.get('password')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Username, Password FROM admin")

        myresult = mycursor.fetchall()

        for x in myresult:
            if(x[0] == username and x[1] == password):
                return render_template("/required.html")

        print(username)
        mycursor.close()
        mydb.close()

    return render_template("admin.html")


@app.route("/required", methods=['GET', 'POST'])
def required_page():
    return render_template("required.html")


@app.route("/runcode/", methods=['GET', 'POST'])
def run_code():
    os.system("python MaskDetection.py")
    return render_template("required.html")

@app.route("/sendemail/", methods=['GET', 'POST'])
def send_email():

    with open('FinalLog.csv','r') as f:
        # myDataList = f.readlines()
        emailList = []
        
        for line in f:
            entry = line.split(',')
            email=entry[1]
            
            if email not in emailList and email!='' and email!='email':
                emailList.append(entry[1])
                time = entry[2]
                date = entry[3]
                path=r'C:\Users\Dell\Desktop\Jainam docs\Deteccion de mascara\Admin\Detected\\'+email.jpeg
                with open(path, 'rb') as fp:
                    msg.add_related(
                    fp.read(), 'image', 'jpeg', cid=attachment_cid)

                mail.send_message('Notification',sender ='projectsupervisor124@gmail.com', recipients = [email], body='Detected at : '+time+' on Date : '+date)        
                
    print(emailList)
    
    return render_template("required.html")


if __name__ == "__main__":
    app.run(debug=True)
