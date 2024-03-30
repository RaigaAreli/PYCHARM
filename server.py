from flask import Flask, render_template, request
from waitress import serve
from main import read_chat_log, display_grades, calculate_grade_percentage  # Import the functions from your main Python file

app = Flask(__name__)

# Route to render the upload form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and display results
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read the contents of the uploaded file
            chat_log_content = file.read().decode('utf-8')

            # Process the chat log to get participation grades
            participation_grades = read_chat_log(chat_log_content)

            # Calculate grade percentage
            grades = calculate_grade_percentage(participation_grades)

            # Display grades
            display_grades()

            # Render the results template with participation grades and percentages
            return render_template('results.html', participation_grades=participation_grades, grades=grades)
        else:
            return render_template('index.html', error='No file uploaded.')
    return render_template('index.html', error='Please select a file.')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
