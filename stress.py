from flask import Flask, jsonify

app = Flask(__name__)

# Define the list of questions
questions = [
    {
        'question': 'Body humidity in percent?',
        'options': []
    },

    {
        'question': 'Body temperature in Fahrenheit',
        'options': []
    },

    {
        'question': 'How many steps have you taken today?',
        'options': []
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070, debug=True)
