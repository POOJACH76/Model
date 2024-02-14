from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'Age',
        'options': []
    },
    {
        'question': 'Gender',
        'options': ['male', 'female']
    },
    {
        'question': 'Have you witnessed negative consequences for coworkers with mental health conditions at your workplace?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Would you discuss a mental health issue with your direct supervisor(s)?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Are you willing to discuss a mental health issue with your coworkers?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Is it easy for you to take medical leave for a mental health condition?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Does your employer support mental health awareness and help-seeking?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Are you working in a tech company?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Do you feel any types of work interfere on your workplace?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Do you have any family history related to mental health?',
        'options': ['yes', 'no']
    },
    {
        'question': 'Are you self-employed?',
        'options': ['yes', 'no']
    }
]

user_responses = {}


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
