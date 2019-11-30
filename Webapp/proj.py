import os
import summary
from flask import Flask, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def render_summary():    
    return render_template('summary.html')

@app.route('/', methods=['POST'])
def render_summary_result():
    link = request.form['link']
    slidervalue = request.form['myRange']
    summary= getSummary(link, slidervalue)
    return link + slidervalue
    #ALEX !!! write the getSummary(String link) function and then this will return getSummary(link) instead of just link
    

if __name__ == "__main__":
    app.run(port=5000)



