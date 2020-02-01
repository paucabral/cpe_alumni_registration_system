from flask import Flask, render_template, url_for, jsonify, request, json
import smtplib

app = Flask(__name__)

gmail_user = 'tip.cpealumni@gmail.com'
gmail_password = 'cpealumni'

@app.route('/post/email', methods=['POST'])
def index():
    
    fname = request.json['fname']
    lname = request.json['lname']
    email = request.json['email']

    sent_from = gmail_user
    to = email
    subject = "CPE Alumni Registration"
    msg = "Hi {} {}. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".format(fname, lname)
    
    message = "Subject: {}\n\n{}".format(subject, msg)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print(sent_from)
        print(to)
        print('Email sent!')
        return jsonify({"Status":"Sent"})
    except:
        print('Error!')
        return jsonify({"Status":"Failed"})


if __name__ == "__main__":
    app.run(debug = True)