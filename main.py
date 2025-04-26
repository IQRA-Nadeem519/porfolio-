# app.py
from flask import Flask, render_template,url_for,send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume-pdf')
def show_pdf():
    return send_file('static/Resume.pdf',mimetype='application/pdf')

@app.route('/')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)