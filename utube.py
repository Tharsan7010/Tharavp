from flask import Flask,render_template,request
app = app.app
import mysql.connector

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Jaish007@#"
app.config['MYSQL_DB'] = "Thar"

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        section = request.form['section']
        location = request.form['location']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO Thar (name,grade,section,location) VALUES (%s,%s,%s,%s)",(name,grade,section,location))
     
        mysql.connection.commit()

        cur.close()

        return "Thank You"
    
    return render_template('form.html') 
   

if __name__=="__main__":
    app.run(debug=True)
