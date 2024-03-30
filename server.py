from flask import Flask, render_template, request
from waitress import serve
from main import process_chat_log  # Import the function from your main Python file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            chat_log_content = file.read().decode('utf-8')
            # Call the function to process the uploaded chat log
            participation_grades = process_chat_log(chat_log_content)
            return render_template('results.html', participation_grades=participation_grades)
    return render_template('index.html', error='Please select a file.')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
