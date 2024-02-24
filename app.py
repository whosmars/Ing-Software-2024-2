from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_usuario import *
from model.model_pelicula import *
from model.model_renta import *

from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta



#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@locfrom alchemyClasses.Usuario import Usuarioalhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Ver registros")
        print("2. Filtrar registros por ID")
        print("3. Actualizar nombre o fecha")
        print("4. Eliminar registros")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ver_menu()
        elif opcion == '2':
            filtrar_por_id_menu()
        elif opcion == '3':
            modificar_registro_menu()
        elif opcion == '4':
            menu_eliminacion()
        elif opcion == '5':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def ver_menu():
    while True:
        print("\nMenú de Visualización:")
        print("1. Ver todos los registros de Usuarios")
        print("2. Ver todos los registros de Películas")
        print("3. Ver todos los registros de Rentas")
        print("4. Salir del submenú")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("Mostrando todos los registros de Usuarios...")
            ver_usuarios()
        elif opcion == '2':
            print("Mostrando todos los registros de Películas...")
            ver_peliculas()
        elif opcion == '3':
            print("Mostrando todos los registros de Rentas...")
            ver_rentar()
        elif opcion == '4':
            print("Saliendo del submenú de visualización...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def filtrar_por_id_menu():
    while True:
        print("\nMenú de Filtrado por ID:")
        print("1. Filtrar Usuario por ID")
        print("2. Filtrar Película por ID")
        print("3. Filtrar Renta por ID")
        print("4. Salir del submenú")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_usuario = input("Ingresa el ID del Usuario a filtrar: ")
            print(f"Filtrando Usuario por ID: {id_usuario}")
            ver_usuario_por_id(id_usuario)
        elif opcion == '2':
            id_pelicula = input("Ingresa el ID de la Película a filtrar: ")
            print(f"Filtrando Película por ID: {id_pelicula}")
            ver_pelicula_por_id(id_pelicula)
        elif opcion == '3':
            id_renta = input("Ingresa el ID de la Renta a filtrar: ")
            print(f"Filtrando Renta por ID: {id_renta}")
            ver_renta_por_id(id_renta)
        elif opcion == '4':
            print("Saliendo del submenú de filtrado por ID...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def modificar_registro_menu():
    while True:
        print("\nMenú de Modificación:")
        print("1. Modificar nombre de Usuario por ID")
        print("2. Modificar nombre de Película por ID")
        print("3. Modificar fecha de Renta por ID")
        print("4. Salir del submenú")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_usuario = input("Ingresa el ID del Usuario a modificar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre del Usuario: ")
            modificar_nombre_usuario(id_usuario, nuevo_nombre)
        elif opcion == '2':
            id_pelicula = input("Ingresa el ID de la Película a modificar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre de la Película: ")
            modificar_nombre_pelicula(id_pelicula, nuevo_nombre)
        elif opcion == '3':
            id_renta = input("Ingresa el ID de la Renta a modificar: ")
            nueva_fecha = input("Ingresa la nueva fecha de la Renta (formato YYYY-MM-DD): ")
            modificar_fecha_renta(id_renta, nueva_fecha)
        elif opcion == '4':
            print("Saliendo del submenú de modificación...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menu_eliminacion():
    while True:
        print("\nMenú de Eliminación:")
        print("1. Usuarios")
        print("2. Películas")
        print("3. Rentas")
        print("4. Salir del submenú")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            submenu_eliminacion_usuarios()
        elif opcion == '2':
            submenu_eliminacion_peliculas()
        elif opcion == '3':
            submenu_eliminacion_rentas()
        elif opcion == '4':
            print("Saliendo del submenú de eliminación...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def submenu_eliminacion_usuarios():
    while True:
        print("\nMenú de Eliminación de Usuarios:")
        print("1. Eliminar un Usuario por ID")
        print("2. Eliminar todos los Usuarios")
        print("3. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_usuario = input("Ingresa el ID del Usuario a eliminar: ")
            eliminar_usuario_y_rentas_por_id(id_usuario)
        elif opcion == '2':
            print("Eliminando todos los Usuarios...")
            eliminar_todos_los_usuarios_y_sus_rentas()
        elif opcion == '3':
            break

def submenu_eliminacion_peliculas():
    while True:
        print("\nMenú de Eliminación de Películas:")
        print("1. Eliminar una Película por ID")
        print("2. Eliminar todas las Películas")
        print("3. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_pelicula = input("Ingresa el ID de la Película a eliminar: ")
            eliminar_pelicula_y_rentas_por_id(id_pelicula)
        elif opcion == '2':
            print("Eliminando todas las Películas...")
            eliminar_todas_las_peliculas_y_sus_rentas()
        elif opcion == '3':
            break

def submenu_eliminacion_rentas():
    while True:
        print("\nMenú de Eliminación de Rentas:")
        print("1. Eliminar una Renta por ID")
        print("2. Eliminar todas las Rentas")
        print("3. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_renta = input("Ingresa el ID de la Renta a eliminar: ")
            eliminar_renta_por_id(id_renta)
        elif opcion == '2':
            print("Eliminando todas las Rentas...")
            eliminar_todas_las_rentas()
        elif opcion == '3':
            break



if __name__ == '__main__':
    with app.app_context():
        print("Conectado con exito a la base de datos!")
        menu()