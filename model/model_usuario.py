from alchemyClasses.Usuario import Usuario
from alchemyClasses.Renta import Renta
from alchemyClasses import db

def ver_usuarios():
    for usuario in Usuario.query.all():
        print(usuario)
        print("----------------------------")

def ver_usuario_por_id(id_usuario):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        print(usuario)
    else:
        print(f'No se encontró el usuario con ID {id_usuario}')

def modificar_nombre_usuario(id_usuario, nuevo_nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        usuario.nombre = nuevo_nombre
        db.session.commit()
        print(f'Nombre del usuario con ID {id_usuario} actualizado a {nuevo_nombre}')
    else:
        print(f'No se encontró el usuario con ID {id_usuario}')

def eliminar_usuario_y_rentas_por_id(id_usuario):
    # Primero, eliminar o actualizar registros en rentar que referencian a este usuario
    rentas = Renta.query.filter_by(idUsuario=id_usuario).all()
    for renta in rentas:
        db.session.delete(renta)
    
    # Luego, eliminar el usuario
    usuario = Usuario.query.get(id_usuario)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print(f'Usuario con ID {id_usuario} y todas sus rentas asociadas han sido eliminados.')
    else:
        print(f'Usuario con ID {id_usuario} no encontrado.')



def eliminar_todos_los_usuarios_y_sus_rentas():
    # Eliminar todas las rentas primero
    db.session.query(Renta).delete()
    
    # Luego, eliminar todos los usuarios
    db.session.query(Usuario).delete()
    
    db.session.commit()
    print('Todos los usuarios y sus rentas asociadas han sido eliminados.')
