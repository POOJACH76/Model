from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'Age in years',
        'options': []
    },
    {
        'question': 'Upper value of Blood Pressure in mmHg',
        'options': []
    },
    {
        'question': 'Lower value of Blood Pressure in mmHg',
        'options': []
    },
    {
        'question': 'Blood glucose levels(mmol/L)',
        'options': []
    },
    {
        'question': 'BodyTemp in fohrenheit',
        'options': []
    },
    {
        'question': 'A normal resting heart rate in beats per minute?',
        'options': []
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8040, debug=True)
