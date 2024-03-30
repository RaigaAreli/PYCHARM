from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Process the uploaded file here
            return 'File uploaded successfully'
    return 'No file uploaded'

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
