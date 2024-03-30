from flask import Flask, render_template, request
from waitress import serve
from main import read_chat_log, display_grades, calculate_grade_percentage  # Import the functions from your main Python file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
