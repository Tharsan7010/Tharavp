from flask import Flask, render_template, request, redirect
from openpyxl import Workbook

app = Flask(__name__)

# Use an in-memory list to store the data (replace this with a database in a real-world scenario)
data_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        grade = request.form['grade']
        section = request.form['section']
        location = request.form['location']

        # Append the data to the list
        data_list.append([name, grade, section, location])

        # Create or load the Excel workbook
        workbook = Workbook()
        sheet = workbook.active

        # Write headers
        sheet.append(['Name', 'Grade', 'Section', 'Location'])

        # Write data
        for data_row in data_list:
            sheet.append(data_row)

        # Save the workbook to a file (replace 'data.xlsx' with your desired filename)
        workbook.save('collect.xlsx')

    return render_template('form.html', data_list=data_list)

if __name__ == '__main__':
    app.run(debug=True)
