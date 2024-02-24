from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)   
    nombre = Column(String(200), nullable= False)
    password = Column(String(64), nullable=False)
    email = Column(String(500), nullable=True, default=None)
    profilePicture = Column(String(64), nullable=True)
    superUser = Column(Integer, nullable=True, default=None)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200), nullable=True)


    def __init__(self, nombre, apPat, password, apMat=None, email=None, profile_picture = None, super_user = None):
        self.nombre = nombre
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = super_user
        self.apPat = apPat
        self.apMat = apMat

    def __str__(self):
        return f'ID usuario: {self.idUsuario}\nNombre:{self.nombre}\napPat:{self.apPat}\napMat:{self.apMat}\npassword:{self.password}\nemail:{self.email}\nsuperUser:{self.superUser}'