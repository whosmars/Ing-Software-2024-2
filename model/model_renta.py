from alchemyClasses.Renta import Renta
from alchemyClasses import db
from datetime import datetime

def ver_rentar():
    for renta in Renta.query.all():
        print(renta)
        print("----------------------------")


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

