from sqlalchemy import Column, Integer, String, Boolean, LargeBinary

from alchemyClasses import db

#Clase que representa a un usuario, se cambio el atributo de superUser por un valor booleano
class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)   
    nombre = Column(String(200), nullable= False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200), nullable=True)
    password = Column(String(64), nullable=False)
    email = Column(String(500), nullable=True, default=None)
    profilePicture = Column(String(64), nullable=True)
    superUser = Column(Boolean, default=None)


    def __init__(self, nombre, apPat, password, apMat=None, email=None, profile_picture = None, superUser = None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = superUser
        
    def __str__(self):
        return f'ID usuario: {self.idUsuario}\nNombre:{self.nombre}\napPat:{self.apPat}\napMat:{self.apMat}\npassword:{self.password}\nemail:{self.email}\nsuperUser:{self.superUser}'