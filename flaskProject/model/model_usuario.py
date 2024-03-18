from alchemyClasses.Usuario import Usuario
from alchemyClasses.Renta import Renta
from alchemyClasses import db

#Regresa todos los usuarios de la base de datos
def ver_usuarios():
    return Usuario.query.all()

def verificar_usuario_actualizar(id):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    return usuario

#Esta funcion regresa el usuario con el id dado
def ver_usuario_por_id(id_usuario):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    return usuario

def modificar_nombre_usuario(id_usuario, nuevo_nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        usuario.nombre = nuevo_nombre
        db.session.commit()
        print(f'Nombre del usuario con ID {id_usuario} actualizado a {nuevo_nombre}')
    else:
        print(f'No se encontró el usuario con ID {id_usuario}')

#Se eliminan las rentas asociadas al usuario y luego se elimina el usuario
def eliminar_usuario_y_rentas_por_id(id):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    if usuario:
        Renta.query.filter(
            Renta.idUsuario == id
        ).delete()
        db.session.delete(usuario)
        db.session.commit()
        print("El usuario y todas sus rentas se eliminaron con exito")
        return True
    else:
        print("El usuario con el id: " + str(id) + " no existe")
        return False

def eliminar_todos_los_usuarios_y_sus_rentas():
    # Eliminar todas las rentas primero
    db.session.query(Renta).delete()
    # Luego, eliminar todos los usuarios
    db.session.query(Usuario).delete()
    db.session.commit()
    print('Todos los usuarios y sus rentas asociadas han sido eliminados.')

#Se inserta un usuario en la base de datos, se hace un try catch para manejar errores
def insertar_usuario(nombre, ap_pat, ap_mat, password, super_user, email):
    try:
        usuario = Usuario(
            nombre=nombre,
            apPat=ap_pat,
            apMat=ap_mat,
            password=password,
            email=email,
            superUser=super_user
        )
        db.session.add(usuario)
        db.session.commit()
        print('Usuario insertado con éxito')
        return True
    except Exception as e:
        db.session.rollback()
        print(f'Error al insertar el usuario: {e}')
        #En caso de error, regresa False
        return False
    

# Se actualiza un usuario en la base de datos, se hace un try catch para manejar errores
def actualiza_usuario(
    id, nombre, apPat, password, super_user, apMat, email, profile_picture=None
):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    if usuario:
        usuario.nombre = nombre
        usuario.apPat = apPat
        usuario.password = password
        usuario.superUser = super_user
        usuario.apMat = apMat
        usuario.email = email
        #usuario.profilePicture = profile_picture
        db.session.commit()
        print("El usuario se actualizò con exito")
        return usuario
    else:
        print("El usuario con el id: " + str(id) + " no existe")
        return usuario