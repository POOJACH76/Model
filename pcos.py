from flask import Flask, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'Age',
        'options': []
    },
    {
        'question': 'Weight (Kg)',
        'options': []
    },
    {
        'question': 'Height (Cm)',
        'options': []
    },
    {
        'question': 'Blood Group',
        'options': []
    },
    {
        'question': 'Pulse_rate_bpm',
        'options': []
    },
    {
        'question': 'RR_breaths_min',
        'options': []
    },
    {
        'question': 'Cycle_length_days',
        'options': []
    },
    {
        'question': 'Marriage_Status_Yrs',
        'options': []
    },
    {
        'question': 'Pregnant',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Hip_inch',
        'options': []
    },
    {
        'question': 'Waist_inch',
        'options': []
    },
    {
        'question': 'Waist_Hip_Ratio',
        'options': []
    },
    {
        'question': 'Weight_gain',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Hair_growth',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Skin_darkening',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Hair_loss',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Pimples',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Fast_food',
        'options': ['Yes', 'No']
    },
    {
        'question': 'Reg_Exercise',
        'options': ['Yes', 'No']
    },
    {
        'question': 'BP_Systolic_mmHg',
        'options': []
    },
    {
        'question': 'BP_Diastolic_mmHg',
        'options': []
    }
]


@app.route("/questions", methods=["GET"])
def get_all_questions():
    return jsonify(questions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8040, debug=True)
