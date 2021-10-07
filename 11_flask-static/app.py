# Team Toast
# Sean Ging, Haotian Gan, Aryman Goenka, Tomas Acuna (Duckies: Friedrich, Cinnamon, Untitled, Llamy)
# SoftDev
# K11: Some Things Never Change / Serving Static Files
# 10-06-2021

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
