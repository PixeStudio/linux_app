from flask import Flask, render_template

app = Flask(__name__)

# Main Page

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/about")

def about():
    return render_template("about.html")

@app.route("/add")

def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
