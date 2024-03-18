from flask import Blueprint, request, render_template, flash, redirect
from model.model_renta import *

renta_blueprint = Blueprint("renta", __name__, url_prefix="/renta")

@renta_blueprint.route("/", methods=["GET", "POST"])
def menu_renta():
    return render_template('renta.html')

@renta_blueprint.route("/add", methods=["GET", "POST"])
def add_renta():
    if request.method == "POST":
        idUsuario = request.form["idUsuario"]
        idPelicula = request.form["idPelicula"]
        fechaRenta = request.form["fecha_renta"]
        fechaEntrega = request.form["dias_de_renta"]
        estatus = request.form.get("estatus") == "true"
        insercionCorrecta = insertar_renta(
            idPelicula, idUsuario, fechaRenta, fechaEntrega, estatus
        )
        if not insercionCorrecta:
            flash(
                "Error al insertar renta verifique si el id de la película y el id del usuario existen",
                "danger",
            )
        else:
            flash("Renta insertada con éxito", "success")
    return render_template("add_renta.html")

@renta_blueprint.route("show", methods=["GET", "POST"])
def show_renta():
    rentas = ver_rentar()
    return render_template("show_renta.html", rentas=rentas)

@renta_blueprint.route("/update", methods=["GET", "POST"])
def update_renta():
    if request.method == "POST":
        idUsuario = request.form["idUsuario"]
        idPelicula = request.form["idPelicula"]
        estatus = request.form.get("estatus") == "true"
        actualizacionCorrecta = actualizar_renta(
             idPelicula, idUsuario, estatus
        )
        if not actualizacionCorrecta:
            flash(
                "Error al actualizar renta verifique si el id de la película y el id del usuario existen",
                "danger",
            )
        else:
            flash("Renta actualizada con éxito", "success")
    return render_template("update_renta.html")

