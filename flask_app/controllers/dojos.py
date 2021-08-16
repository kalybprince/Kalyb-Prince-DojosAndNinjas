from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    """render index page"""
    print('*'*80)
    print("/dojos")
    dojos = Dojo.show_all()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)

@app.route('/new_dojo', methods=["POST"])
def new_dojo():
    """create new dojo"""
    print('*'*80)
    print("/new_dojo")
    print(request.form)
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route('/dojos/<int:num>')
def display_dojo(num):
    """display ninjas of a given dojo"""
    print('*'*80)
    print(f"/dojos/{num}")
    dojos = Dojo.show_all()
    data = {"id": f"{num}"}
    dojos_with_ninjas = Dojo.get_dojo_with_ninjas(data)
    for each_ninja in dojos_with_ninjas.ninjas:
        print(each_ninja.first_name)
    return render_template("dojo_show.html", dojos=dojos, dojos_with_ninjas=dojos_with_ninjas)
