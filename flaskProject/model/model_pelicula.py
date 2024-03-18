from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db

#Regresa todas las peliculas de la base de datos
def ver_peliculas():
    return Pelicula.query.all()

def ver_pelicula_por_id(id_pelicula):
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
    return pelicula


def modificar_nombre_pelicula(id_pelicula, nuevo_nombre):
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
    if pelicula:
        pelicula.nombre = nuevo_nombre # Asumiendo que la columna se llama 'nombre'
        db.session.commit()
        print(f'Nombre de la película con ID {id_pelicula} actualizado a {nuevo_nombre}')
    else:
        print(f'No se encontró la película con ID {id_pelicula}')


def eliminar_pelicula_y_rentas_por_id(id):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    if pelicula:
        Renta.query.filter(
            Renta.idPelicula == id
        ).delete()  # Elimino las rentas en las que esta
        db.session.delete(pelicula)
        db.session.commit()
        print("La pelicula y todas sus rentas se eliminaron con exito")
        return True
    else:
        print("La pelicula con el id: " + str(id) + " no existe")
        return False


def eliminar_todas_las_peliculas_y_sus_rentas():
    # Eliminar todas las rentas primero
    db.session.query(Renta).delete()
    
    # Luego, eliminar todas las películas
    db.session.query(Pelicula).delete()
    
    db.session.commit()
    print('Todas las películas y sus rentas asociadas han sido eliminadas.')

#Se inserta una pelicula en la base de datos, se hace un try catch para manejar errores
def insertar_pelicula(nombre, genero, duracion, inventario):
    try:
        pelicula = Pelicula(
            nombre = nombre,
            genero = genero,
            duracion = duracion,
            inventario = inventario
        )
        db.session.add(pelicula)
        db.session.commit()
        print('Pelicula insertada con exito')
        return True
    except Exception as e:
        db.session.rollback()
        print(f'Error al insertar el usuario: {e}')
        return False
    
# Se actualiza una pelicula en la base de datos, se hace un try catch para manejar errores
def actualiza_pelicula(id, nombre, genero, inventario, duracion):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    if pelicula:
        pelicula.nombre = nombre
        pelicula.genero = genero
        pelicula.inventario = inventario
        pelicula.duracion = duracion
        db.session.commit()
        print("La actualizacion del nombre fue exitosa!!")
        return pelicula
    else:
        print("La pelicula con el id: " + str(id) + " No existe")
        return pelicula