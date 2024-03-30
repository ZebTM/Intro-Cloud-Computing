from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    email = request.form['email']
    return render_template('questions.html', firstName=firstName, lastName=lastName, email=email)

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    if question == 'football_team':
        return "Yes, the college has a football team."
    elif question == 'computer_science_major':
        return "Yes, Computer Science is offered as a major."
    elif question == 'tuition':
        return "The in-state tuition is $XXXXX."
    elif question == 'housing':
        return "Yes, the college provides on-campus housing."
    else:
        return "Sorry, I couldn't understand your question."
    
@app.route('/finish', methods=['POST'])
def finish():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    return render_template('finish.html', firstName=firstName, lastName=lastName, email=email)


if __name__ == '__main__':
    app.run(debug=True)
