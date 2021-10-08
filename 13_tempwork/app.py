  # Team BurnedToast
# Sean Ging, Tomas Acuna, Naomi Naranjo (Duckies: Friedrich, )
# SoftDev
# K13: Template for Success/ Jinja2 Templating
# 10-08-2021

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/occupyflaskst")
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument?

if __name__ == "__main__":
    app.debug = True
    app.run()
