"""
    This script runs the Python Flask web application
    of the simulator. Please see the README for detailed
    instructions.
"""
#======================Imports========================
from flask import Flask, render_template, request, redirect, url_for
from simulator import start_simulation
from utils.procPlot import main
#=====================================================

#======================Setup==========================
app = Flask(__name__)

# Prevent cached responses
# The function below was taken from https://stackoverflow.com/questions/47376744/how-to-prevent-cached-response-flask-server-using-chrome
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
#=====================================================

#====================Home Route=======================
@app.route("/")
def home():
    return render_template('home.html')
#=====================================================

#===================Results Route=====================
@app.route("/chart")
def chart():
    return render_template('chart.html')
#=====================================================

#================Submit Inputs========================
@app.route("/simulate", methods=['POST'])
def simulate():
    try:
        #Start simulation
        start_simulation(int(request.form["timer"]), int(request.form["processNum"]))
        #Generate graphs from raw data
        main()
        #Direct to the chart page
        return redirect(url_for('chart'))
    except Exception as e:
        print("Error encountered: " + str(e)) 
#=====================================================

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8000)
#=====================================================