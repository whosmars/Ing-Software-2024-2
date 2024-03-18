from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, default=1, nullable=True,)
    inventario = Column(Integer, default=1, nullable=False)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'IdPelicula:{self.idPelicula}\nNombre:{self.nombre}\ngenero:{self.genero}\ninventario:{self.inventario}\nduracion:{self.duracion}'