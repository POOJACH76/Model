from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'How many hours did you stay up last night?',
        'options': []
    },
    {
        'question': 'What is your current pressure level?',
        'options': ['Low', 'Medium', 'High', 'Very High']
    },
    {
        'question': 'How many cups of coffee do you consume in a day?',
        'options': []
    },
    {
        'question': 'How many hours a day does your brain work actively?',
        'options': []
    },
    {
        'question': 'Which shampoo brand do you most frequently use?',
        'options': ['Pantene', 'Head & Shoulders']
    },
    {
        'question': 'Did you go swimming?',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Do you wash your hair regularly?',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Dandruff level',
        'options': ['None', 'Few', 'Many']
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8060, debug=True)
