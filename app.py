from flask import Flask, request, render_template
import openpyxl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    class = request.form.get('class')
    section = request.form.get('section')
    location = request.form.get('location')
    

    # Store the data in an Excel file
    workbook = openpyxl.load_workbook('student_data.xlsx')
    worksheet = workbook.active
    worksheet.append([name, class, section, location])
    workbook.save('student_data.xlsx')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
