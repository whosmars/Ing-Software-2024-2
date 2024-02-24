from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db

def ver_peliculas():
    for pelicula in Pelicula.query.all():
        print(pelicula)
        print("----------------------------")


def ver_pelicula_por_id(id_pelicula):
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
    if pelicula:
        print(pelicula)
    else:
        print(f'No se encontró la película con ID {id_pelicula}')


def modificar_nombre_pelicula(id_pelicula, nuevo_nombre):
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
    if pelicula:
        pelicula.nombre = nuevo_nombre # Asumiendo que la columna se llama 'nombre'
        db.session.commit()
        print(f'Nombre de la película con ID {id_pelicula} actualizado a {nuevo_nombre}')
    else:
        print(f'No se encontró la película con ID {id_pelicula}')


def eliminar_pelicula_y_rentas_por_id(id_pelicula):
    # Primero, eliminar registros en renta que referencian a esta película
    rentas = Renta.query.filter_by(idPelicula=id_pelicula).all()
    for renta in rentas:
        db.session.delete(renta)
    
    # Luego, eliminar la película
    pelicula = Pelicula.query.get(id_pelicula)
    if pelicula:
        db.session.delete(pelicula)
        db.session.commit()
        print(f'Película con ID {id_pelicula} y todas sus rentas asociadas han sido eliminadas.')
    else:
        print(f'Película con ID {id_pelicula} no encontrada.')

def eliminar_todas_las_peliculas_y_sus_rentas():
    # Eliminar todas las rentas primero
    db.session.query(Renta).delete()
    
    # Luego, eliminar todas las películas
    db.session.query(Pelicula).delete()
    
    db.session.commit()
    print('Todas las películas y sus rentas asociadas han sido eliminadas.')



