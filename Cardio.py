from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'Age in years',
        'options': []
    },
    {
        'question': 'Gender',
        'options': []
    },
    {
        'question': 'Height (Cm)',
        'options': []
    },
    {
        'question': 'Weight (kg)',
        'options': []
    },
    {
        'question': 'Upper blood pressure',
        'options': []
    },
    {
        'question': 'Lower blood pressure',
        'options': []
    },
    {
        'question': 'Cholesterol',
        'options': []
    },
    {
        'question': 'Glucose',
        'options': []
    },
    {
        'question': 'Smoke',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Alcoholic',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Physical Activities',
        'options': ['Yes', 'No']
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010, debug=True)
