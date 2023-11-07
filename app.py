from flask import Flask, render_template, request, redirect
import openpyxl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    grade = request.form.get('grade')
    section = request.form.get('section')
    location = request.form.get('location')

    # Store the data in an Excel file
    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = workbook.active
    worksheet.append([name, grade, section, location])
    workbook.save('data.xlsx')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
