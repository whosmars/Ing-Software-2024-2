from flask import Blueprint, request, render_template, flash, url_for, redirect
from model.model_usuario import *

usuario_blueprint = Blueprint("usuario", __name__, url_prefix="/usuario")

@usuario_blueprint.route("/", methods=["GET", "POST"])
def menu_usuario():
    return render_template('usuario.html')

@usuario_blueprint.route("/add", methods=["GET", "POST"])
def add_usuario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apPat = request.form["apPat"]
        apMat = request.form["apMat"]
        superUser = 'superUser' in request.form  # Cambiado para verificar la presencia de la clave 'superUser'
        email = request.form["correo"]
        password = request.form["password"]
        profile_picture = request.files["profile_picture"]
        insercionCorrecta = insertar_usuario(
            nombre, apPat, apMat, password, superUser, email
        )
        if not insercionCorrecta:
            flash(
                "Error al insertar usuario verifique si el correo ya esta registrado",
                "danger",
            )
        else:
            flash("Usuario insertado con exito", "success")
    return render_template("add_usuario.html")

@usuario_blueprint.route("show", methods=["GET", "POST"])
def show_usuario():
    usuarios = ver_usuarios()
    return render_template("show_usuario.html", usuarios=usuarios)

@usuario_blueprint.route("/checkID", methods=["GET", "POST"])
def check_id_usuario():
    if request.method == "POST":
        idUsuario = request.form["idUsuario"]
        usuario = ver_usuario_por_id(idUsuario)
        if usuario:
            return render_template("update_usuario.html", usuario=usuario)
        else:
            flash("No se encontro el usuario con el id: " + idUsuario, "danger")
            return render_template("check_id_usuario.html")
    else:
        return render_template("check_id_usuario.html")
    
@usuario_blueprint.route("/update", methods=["GET", "POST"])
def update_usuario():
    if request.method == "POST":
        idUsuario = request.form["idUsuario"]
        nombre = request.form["nombre"]
        apPat = request.form["apPat"]
        apMat = request.form["apMat"]
        superUser = request.form.get("superUser") == "true"
        email = request.form["correo"]
        password = request.form["password"]
        #profile_picture = request.files["profile_picture"]
        usuario = actualiza_usuario(
            idUsuario, nombre, apPat, password, superUser, apMat, email
        )
        if usuario:
            flash("Usuario actualizado con exito", "success")
        else:
            flash("No se encontro el usuario con el id: " + idUsuario, "danger")
    return render_template("update_usuario.html", usuario=usuario)

@usuario_blueprint.route("/delete", methods=["GET", "POST"])
def delete_usuario():
    if request.method == "POST":
        idUsuario = request.form["idUsuario"]
        usuario = eliminar_usuario_y_rentas_por_id(idUsuario)
        if usuario:
            flash("Usuario eliminado con exito", "success")
        else:
            flash("No se encontro el usuario con el id: " + idUsuario, "danger")
    return render_template("delete_usuario.html")