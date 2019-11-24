import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')

@app.route('/summary')
def render_summary():
    return render_template('summary.html')

@app.route('/summary', methods=['POST'])
def render_summary_result():
    link = request.form['link']
    return link

if __name__ == "__main__":
    app.run(port=5000)

