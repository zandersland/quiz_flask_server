from flask import Flask, render_template, request
import os
import csv
import random

app = Flask(__name__)
app.secret_key = b'CHANGEME!!!!!!!!!!!!'


@app.route('/')
def index():
    topic_choices = []
    dirs = os.listdir('./csv_files')
    for _dir in dirs:
        if os.path.isdir(f'./csv_files/{_dir}'):
            topic_choices.append(_dir)
    return render_template('index.html', topic_choices=topic_choices)


@app.route('/topic')
def topic():
    topic_choice = request.args.get('topic')
    quiz_choices = []
    if topic_choice is not None:
        dirs = os.listdir(f'./csv_files/{topic_choice}')
        quiz_choices = dirs
    return render_template('topic.html', quiz_choices=quiz_choices, topic_choice=topic_choice)


@app.route('/quiz')
def quiz():
    quiz_choice = request.args.get('quiz')
    topic_choice = request.args.get('topic')
    rows = []
    if request.args.get('rows') is None:
        if quiz_choice is not None:
            with open(f'./csv_files/{topic_choice}/{quiz_choice}') as f:
                csvreader = csv.reader(f)
                for row in csvreader:
                    rows.append(row)
    else:
        rows = request.args.get('rows')
    random_row = random.choice(rows)
    random.shuffle(rows)
    return render_template('quiz.html', topic_choice=topic_choice, quiz_choice=quiz_choice, rows=rows, random_row=random_row)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=50003, threaded=True)
