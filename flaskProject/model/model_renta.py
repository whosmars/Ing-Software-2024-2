from alchemyClasses.Renta import Renta
from alchemyClasses import db
from datetime import datetime
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Usuario import Usuario

#Regresa todas las rentas
def ver_rentar():
    return Renta.query.all()

def ver_renta_por_id(id_renta):
    renta = Renta.query.filter_by(idRentar=id_renta).first()
    if renta:
        print(renta)
    else:
        print(f'No se encontró la renta con ID {id_renta}')

def modificar_fecha_renta(id_renta, nueva_fecha):
    renta = Renta.query.filter_by(idRentar=id_renta).first()
    if renta:
        renta.fechaRenta = datetime.strptime(nueva_fecha, '%Y-%m-%d') # Formato de fecha: Año-Mes-Día
        db.session.commit()
        print(f'Fecha de renta con ID {id_renta} actualizada a {nueva_fecha}')
    else:
        print(f'No se encontró la renta con ID {id_renta}')


def eliminar_renta_por_id(id_renta):
    renta = Renta.query.get(id_renta)
    if renta:
        db.session.delete(renta)
        db.session.commit()
        print(f'Renta con ID {id_renta} ha sido eliminada.')
    else:
        print(f'Renta con ID {id_renta} no encontrada.')
    

def eliminar_todas_las_rentas():
    rentas = Renta.query.all()
    for renta in rentas:     
        db.session.delete(renta)
    db.session.commit()
    print("Todos los registros de las rentas se eliminaron correctamente")

#Se inserta una renta en la base de datos. Se revisa que el usuario y la pelicula existan
def insertar_renta(id_pelicula, id_usuario, fecha_renta, fecha_entrega, estatus):
    try:
        nueva_renta = Renta(
            idPelicula=id_pelicula,
            idUsuario=id_usuario,
            fecha_renta=datetime.strptime(fecha_renta, '%Y-%m-%d'),  # Formato de fecha: Año-Mes-Día
            dias_de_renta=fecha_entrega, 
            estatus=estatus #El estatus es independiente de la fecha de entrega
        )
        if not Usuario.query.filter(Usuario.idUsuario == id_usuario).first():
            print(f"No se encontró el usuario con ID {id_usuario}")
            return False
        if not Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first():
            print(f"No se encontró la película con ID {id_pelicula}")
            return False
        db.session.add(nueva_renta)
        db.session.commit()
        print("Renta insertada con éxito")
        return True  #Si no hay errores, regresa True
    except Exception as e:
        db.session.rollback()
        print(f"Error al insertar la renta: {e}")
        return False  #Si hay un error, regresa False
    
#Dada las llaves parciales de la renta, se actualiza el estatus de la renta
def actualizar_renta(idP, idU, estatus):
    renta = Renta.query.filter(Renta.idPelicula == idP and Renta.idUsuario == idU).first()
    if renta:
        renta.estatus = estatus
        db.session.commit()
        print("La actualizacion del estatus fue exitosa!!")
        return renta
    else:
        print("La renta con ID: " + str(id) + " No existe")
        return renta
