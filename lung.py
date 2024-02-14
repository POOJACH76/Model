from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'AGE',
        'options': []
    },
    {
        'question': 'SMOKING',
        'options': ['Yes', 'No']
    },
    {
        'question': 'YELLOW_FINGERS',
        'options': ['Yes', 'No']
    },
    {
        'question': 'ANXIETY',
        'options': ['Yes', 'No']
    },
    {
        'question': 'PEER_PRESSURE',
        'options': ['Yes', 'No']
    },
    {
        'question': 'CHRONIC DISEASE',
        'options': ['Yes', 'No']
    },
    {
        'question': 'FATIGUE',
        'options': ['Yes', 'No']
    },
    {
        'question': 'ALLERGY',
        'options': ['Yes', 'No']
    },
    {
        'question': 'WHEEZING',
        'options': ['Yes', 'No']
    },
    {
        'question': 'ALCOHOL CONSUMING',
        'options': ['Yes', 'No']
    },
    {
        'question': 'COUGHING',
        'options': ['Yes', 'No']
    },
    {
        'question': 'SHORTNESS OF BREATH',
        'options': ['Yes', 'No']
    },
    {
        'question': 'SWALLOWING DIFFICULTY',
        'options': ['Yes', 'No']
    },
    {
        'question': 'CHEST PAIN',
        'options': ['Yes', 'No']
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
