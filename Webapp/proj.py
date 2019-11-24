import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')

@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')


@app.route('/ctof_result')
def render_ctof_result():
        try:
            ctemp_result = float(request.args['cTemp'])
            ftemp_result = ctof(ctemp_result)
            return render_template('ctof_result.html', cTemp=ctemp_result, fTemp=ftemp_result)
        except ValueError:
            return "Sorry: something went wrong."

@app.route('/summary')
def render_summary():
    return render_template('summary.html')


@app.route('/summary_result')
def render_summary_result():
    return render_template('summaryresult.html')



def ctof(ctemp):
    return (ctemp*9/5)+32



if __name__ == "__main__":
    app.run(port=5000)

