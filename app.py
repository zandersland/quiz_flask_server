from flask import Flask, render_template, request
from os import listdir
import csv
import random

app = Flask(__name__)
app.secret_key = b'CHANGEME!!!!!!!!!!!!'


@app.route('/')
def index():
    quiz_choices = listdir('./csv_files')
    return render_template('index.html', quiz_choices=quiz_choices)


@app.route('/quiz')
def quiz():
    quiz_choice = request.args.get('quiz')
    rows = []
    if quiz_choice is not None:
        with open(f'./csv_files/{quiz_choice}') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                rows.append(row)
    random_row = random.choice(rows)
    return render_template('quiz.html', quiz_choice=quiz_choice, rows=rows, random_row=random_row)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=50003, threaded=True)
