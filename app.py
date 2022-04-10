from flask import Flask, render_template, url_for
from flask import redirect, flash
from forms import LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "8278887336f750056db0e2facb82d5ea"

@app.route("/", methods=["GET", "POST"])
def index():
    # LANDING PAGE HAS A TEACHER LOG IN FORM #
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "oyarojared@nyabondomixed"\
            and form.password.data == "code":
            return f'Logged in successfully as {form.username.data}'
        else:
            flash("Incorrect Username or Password!", "danger")
    return render_template("index.html", form=form)

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    return render_template("admin_login.html", form=form)



if "__name__" == "__main__":
    app.run(debug=True)