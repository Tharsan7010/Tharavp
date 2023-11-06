from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

data = []

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    class_name = request.form.get('class')
    section = request.form.get('section')
    location = request.form.get('location')

    data.append({'Name': name, 'Class': class_name, 'Section':section, 'Location':location})

    # Create or update an Excel file to store the data
    df = pd.DataFrame(data)
    df.to_excel('student_data.xlsx', index=False)

    return 'Data has been submitted and stored in Excel.'

if __name__ == '__main__':
    app.run(debug=True)

