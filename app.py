from flask import Flask, request, render_template, redirect, url_for, session
from crystal_ball import CrystalBall
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'your-secret-key'  # For session

crystal_ball = None

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx', 'md'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    global crystal_ball

    if request.method == 'POST':
        # get the file from the request
        file = request.files['document']

        # if a file is selected, read the file content into document
        if file.filename != '' and file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            document = file.read().decode('utf-8')
        else:  # if no file is selected, use the old method
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

# any other routes

if __name__ == "__main__":
    app.run(debug=True)
    