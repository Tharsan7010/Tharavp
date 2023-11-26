from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# In-memory storage for collected data
collected_data = []

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form.get('name')
    grade = request.form.get('grade')
    section = request.form.get('section')
    location = request.form.get('location')

    # Store data in memory
    collected_data.append({'Name': name, 'Grade': grade, 'Section': section, 'Location': location})

    # Redirect to the home page after submission
    return redirect(url_for('form'))

@app.route('/download')
def download():
    # Convert the collected data to a DataFrame
    df = pd.DataFrame(collected_data)

    # Save data to a text file
    text_file_path = 'collect.txt'
    df.to_csv(text_file_path, index=False, sep='\t')

    # Save data to an Excel file
    excel_file_path = 'collect.xlsx'
    df.to_excel(excel_file_path, index=False)

    return f'Data saved to {text_file_path} and {excel_file_path}'

if __name__ == '__main__':
    app.run(debug=True)
