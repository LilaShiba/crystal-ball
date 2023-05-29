from flask import Flask, request, render_template, redirect, url_for
from crystal_ball import CrystalBall

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        
        crystal_ball = CrystalBall()

        document = request.form['document']
        question = request.form['question']
        doc_type = request.form.get('doc_type', 'txt')  # Default doc_type to 'txt' if not provided

        if doc_type.lower() == 'md':
            document = crystal_ball.remove_markdown_syntax(document)

        crystal_ball.document = document
        answers = crystal_ball.answer_question(question)

        return render_template('show_answers.html', answers=answers)
    else:
        return render_template('predict.html')

@app.route('/ask_again')
def ask_again():
    return redirect(url_for('ask'))

if __name__ == "__main__":
    app.run(debug=True)
