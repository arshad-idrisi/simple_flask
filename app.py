from flask import Flask, render_template

app = Flask(__name__)


@app.route("/conditionals_basics/")
def render_conditionals_basics():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)


'''if __name__ == '__main__':
    app.run(debug=True)'''