from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    grade = request.form.get('class')
    section = request.form.get('section')
    location = request.form.get('location')

    with open('data.txt', 'a') as file:
        file.write(f'Name: {name}, Grade: {grade}, Section:{section}, Location:{location}\n')

    return 'Data has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)
