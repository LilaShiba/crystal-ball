from flask import Flask, request, render_template, redirect, url_for, session
from crystal_ball import CrystalBall

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'your-secret-key'  # For session

crystal_ball = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    global crystal_ball

    if request.method == 'POST':
        document = request.form['document']
        question = request.form['question']
        doc_type = request.form.get('doc_type', 'txt')  # Default doc_type to 'txt' if not provided

        # Check if the document has changed or crystal_ball is None
        if crystal_ball is None or document != session.get('document'):
            crystal_ball = CrystalBall()
            if doc_type.lower() == 'md':
                document = crystal_ball.remove_markdown_syntax(document)
            crystal_ball.document = document
            session['document'] = document  # Store the document in session

        answers = crystal_ball.answer_question(question)

        return render_template('show_answers.html', answers=answers)
    else:
        return render_template('predict.html')

@app.route('/ask_again')
def ask_again():
    return redirect(url_for('ask'))

if __name__ == "__main__":
    app.run(debug=True)
