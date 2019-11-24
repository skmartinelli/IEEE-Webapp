import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')

@app.route('/summary')
def render_summary():
    return render_template('summary.html')

@app.route('/summary_result')
def render_summary_result():
    return render_template('summaryresult.html')

if __name__ == "__main__":
    app.run(port=5000)

