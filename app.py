#======================Imports========================
from flask import Flask, render_template, request, redirect, url_for
from simulator import start_simulation
#=====================================================

#======================Setup==========================
app = Flask(__name__)
#=====================================================

#====================Home Route=======================
@app.route("/")
def home():
    return render_template('home.html')
#=====================================================

#================Submit Inputs========================
@app.route("/simulate", methods=['POST'])
def simulate():
    try:
        start_simulation(int(request.form["timer"]), int(request.form["processNum"]))
        return redirect(url_for('home'))
    except Exception as e:
        print("Error encountered: " + str(e)) 
#=====================================================

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
#=====================================================

