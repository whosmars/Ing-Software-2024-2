from flask import Blueprint, request, render_template, flash, url_for, redirect
from model.model_pelicula import *

pelicula_blueprint = Blueprint("pelicula", __name__, url_prefix="/pelicula")

@pelicula_blueprint.route("/", methods=["GET", "POST"])
def menu_pelicula():
    return render_template('pelicula.html')

@pelicula_blueprint.route("/add", methods=["GET", "POST"])
def add_pelicula():
    if request.method == "POST":
        nombre = request.form["nombre"]
        genero = request.form["genero"]
        duracion = request.form["duracion"]
        inventario = request.form["inventario"]
        insercionCorrecta = insertar_pelicula(
            nombre, genero, duracion, inventario
        )
        if not insercionCorrecta:
            flash(
                "Error al insertar usuario verifique si el correo ya esta registrado",
                "danger",
            )
        else:
            flash("Película insertada con éxito", "success")
    return render_template("add_pelicula.html")

@pelicula_blueprint.route("show", methods=["GET", "POST"])
def show_pelicula():
    peliculas = ver_peliculas()
    return render_template("show_pelicula.html", peliculas=peliculas)


@pelicula_blueprint.route("/checkID", methods=["GET", "POST"])
def check_id_pelicula():
    if request.method == "POST":
        idPelicula = request.form["idPelicula"]
        pelicula = ver_pelicula_por_id(idPelicula)
        if pelicula:
            return render_template("update_pelicula.html", pelicula=pelicula)
        else:
            flash("No se encontro la película con el id: " + idPelicula, "danger")
            return render_template("check_id_pelicula.html")
    else:
        return render_template("check_id_pelicula.html")
    
@pelicula_blueprint.route("/update", methods=["GET", "POST"])
def update_pelicula():
    if request.method == "POST":
        idPelicula = request.form["idPelicula"]
        nombre = request.form["nombre"]
        genero = request.form["genero"]
        duracion = request.form["duracion"]
        inventario = request.form["inventario"]
        pelicula = actualiza_pelicula(
            idPelicula, nombre, genero, duracion, inventario
        )
        if pelicula:
            flash("Película actualizada con éxito", "success")
        else:
            flash("No se encontro pelicula con el id: " + idPelicula, "danger")
    return render_template("update_pelicula.html", pelicula=pelicula)

@pelicula_blueprint.route("/delete", methods=["GET", "POST"])
def delete_pelicula():
    if request.method == "POST":
        idPelicula = request.form["idPelicula"]
        pelicula = eliminar_pelicula_y_rentas_por_id(idPelicula)
        if pelicula:
            flash("Película eliminada con éxito", "success")
        else:
            flash("No se encontro pelicula con el id: " + idPelicula, "danger")
    return render_template("delete_pelicula.html")