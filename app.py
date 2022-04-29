from datetime import datetime
from flask import Flask, render_template, url_for
from flask import redirect, flash
from forms import LoginForm
from database import meta, settings, engine
from sqlalchemy.sql import select, insert, delete, update


app = Flask(__name__)
app.config["SECRET_KEY"] = "8278887336f750056db0e2facb82d5ea"
settings.create(engine, checkfirst=True) # CREATE SETTINGS DATABASE


@app.route("/", methods=["GET", "POST"])
def index():
    # LANDING PAGE WITH A TEACHER LOG IN FORM #
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "oyarojared@nyabondomixed"\
            and form.password.data == "code":
            setts = engine.connect().execute(select([settings])).first()
            username = form.username.data
            time = datetime.utcnow()
            return render_template("teacher_dashboard.html", username=username, time=time)
        else:
            flash("Incorrect Username or Password!", "danger")
    return render_template("index.html", form=form)

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    return render_template("admin_login.html", form=form)



if "__name__" == "__main__":
    app.run(debug=True)