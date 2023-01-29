from flask import Flask,render_template, redirect, url_for, request
import pickle
import numpy as np
import pandas as pd
import random 
#why does it say "no module named keras"?

#after the trained model actually gets loaded, 
#I would need a numpy array as input for model.predict function
# how does request.form accept data?
# can I receive the data directly as a numpy array or 
# would I need additional steps to convert it? 
app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        name = random.choice(["yes","no"])

        return redirect(url_for(name))
    
    else: 
        return render_template("index.html")


@app.route("/yes")
def yes():
    rst = "you have diabetes!"
    return f"<h1><center>{rst}</center></h1>"

@app.route("/no")
def no():
    usr = "yon dont pog!"
    return f"<h1>{usr}</h1>"



if __name__== '__main__':
    app.run(debug=True, port = 8000)    