from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime

from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Usuario import Usuario

#Clase que representa a una renta, se cambio estatus por un valor booleano
class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario', ondelete='CASCADE'), nullable= False)   
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula', ondelete='CASCADE'), nullable=False)
    fecha_renta = Column(DateTime, nullable= False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=0)

    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus
        

    def __str__(self):
        usuario= Usuario.query.get(self.idUsuario)
        pelicula = Pelicula.query.get(self.idPelicula)
        return f'ID:{self.idRentar}\nUsuario:{usuario.nombre}\nPelicula:{pelicula.nombre}\nFecha de renta:{self.fecha_renta}\nDias de renta:{self.dias_de_renta}\nEstatus:{self.estatus}'