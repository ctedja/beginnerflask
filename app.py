from flask import Flask, render_template, request, flash

# This command create a class for our app
app = Flask(__name__)
app.secret_key = "test"

# This command creates a route for our app
@app.route("/hello")
def index():
    flash("what's your name!?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)