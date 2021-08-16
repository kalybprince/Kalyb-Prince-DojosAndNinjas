from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    print("*"*80)
    print("/ninjas")
    dojos = Dojo.show_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route("/new_ninja", methods=["POST"])
def make_ninja():
    print("*"*80)
    print("/new_ninja")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "dojos_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    print(request.form)
    return redirect("/ninjas")