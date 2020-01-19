from flask import Flask, render_template, url_for, jsonify, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'registration_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
MySQL = MySQL(app)


# +--------------+--------------+------+-----+---------+----------------+
# | Field        | Type         | Null | Key | Default | Extra          |
# +--------------+--------------+------+-----+---------+----------------+
# | id           | int(11)      | NO   | PRI | NULL    | auto_increment |
# | fname        | varchar(255) | YES  |     | NULL    |                |
# | lname        | varchar(255) | YES  |     | NULL    |                |
# | email        | varchar(255) | YES  |     | NULL    |                |
# | isregistered | tinyint(1)   | YES  |     | NULL    |                |
# | ispaid       | tinyint(1)   | YES  |     | NULL    |                |
# +--------------+--------------+------+-----+---------+----------------+

# conn = MySQL.connection
# cursor = conn.cursor()
# use cursor.execute('MySQL Command') to execute commands
# use conn.commit() to commit MySQL DML commands
# use cursor.fetchall() to capture a list of dictionaries
# use cursor.fetchone() to capture one dictionary


@app.route('/', methods=['POST', 'GET'])
def index():
    conn = MySQL.connection
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT*FROM alumni')
        results = cursor.fetchall()
        return jsonify(results)
    elif request.method == 'POST':
        fname = request.json['fname']
        lname = request.json['lname']
        email = request.json['email']
        isregistered = request.json['isregistered']
        ispaid = request.json['ispaid']
        
        cursor.execute("INSERT INTO alumni(fname, lname) VALUES('{}','{}')".format(fname, lname))
        conn.commit()
        return "check database"


if __name__ == "__main__":
    app.run(debug = True)