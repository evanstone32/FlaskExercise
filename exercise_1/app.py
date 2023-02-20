from flask import Flask, render_template

app = Flask(__name__) #creates a app vairable and sets it to the flask class. __name__ is so that flask knows where to look for files

@app.route("/") #creates an way to the webiste
def index(): #function for code for the assignment
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)