# Team BurnedToast
# Sean Ging, Tomas Acuna, Naomi Naranjo (Duckies: Friedrich, )
# SoftDev
# K13: Template for Success/ render_templates, randomly generating, app.route
# 10-08-2021

from flask import Flask, render_template
import random
import csv
app = Flask(__name__)

#Function to read csv file and transfer it to an approriate dictionary
def readfile(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    header = next(csvreader)
    occupations = {}
    for row in csvreader:
        if header[1] != row[1]:
            if row[0] != "Total":
                occupations[row[0]] = row[1]
    file.close()
    return occupations

#Using the weights provided in percentages, generate a randomly selected occupation
def generateRandom(occupations):
    ran = random.random() * 100
    for row in occupations:
        holder = occupations.get(row)
        ran -= float(holder)
        if ran <= 0:
            return row
    return "Unemployed" #if user never reaches 0, they are unemployed

@app.route("/occupyflaskst")
def funct():
    return render_template("tablified.html", foo="Random Occupation", tnpg = "BurnedToast: Sean Ging, Tomas Acuna, Naomi Naranjo" ,jc = list(csv.reader(open("data/occupations.csv", "r")))[1:-1], chosen= generateRandom(readfile("data/occupations.csv")))
if __name__ == "__main__":
    app.debug = True
    app.run()
