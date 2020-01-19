from flask import Flask, render_template, url_for, jsonify, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'registration_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
MySQL = MySQL(app)

@app.route('/get/number-paid', methods=['GET'])
def index():
    conn = MySQL.connection
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(id) AS registeredAlumni FROM alumni WHERE isregistered = 1 AND ispaid = 1')
    names = cursor.fetchone()
    return jsonify(names)

if __name__ == "__main__":
    app.run(debug = True)