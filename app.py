from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    class_name = request.form.get('class')
    section = request.form.get('section')
    location = request.form.get('location')

    with open('data.txt', 'a') as file:
        file.write(f'Name: {name}, Class: {class_name}, Section:{section}, Location:{location}\n')

    return 'Data has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)
