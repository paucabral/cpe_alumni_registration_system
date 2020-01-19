from flask import Flask, render_template, url_for, jsonify, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'registration_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
MySQL = MySQL(app)

@app.route('/post/paid', methods=['POST'])
def index():
    conn = MySQL.connection
    cursor = conn.cursor()
    
    fname = request.json['fname']
    lname = request.json['lname']
    email = request.json['email']

    cursor.execute("UPDATE alumni SET ispaid = 1 WHERE fname = '{}' AND lname = '{}' AND email = '{}' AND isregistered = 1".format(fname, lname, email))
    conn.commit()
    
    return "return render_template() here"


if __name__ == "__main__":
    app.run(debug = True)