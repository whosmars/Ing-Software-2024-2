import pymysql.cursors
import random as rd
from faker import Faker

try:
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='lab',
                                password='Developer123!',
                                database='lab_ing_software',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    fake = Faker()
    print("La conexion con la base de datos ha sido exitosa!!")
except Exception as failedconnection:
    print(f"No se ha podido conectar con la base de datos debido a : {failedconnection}")

def insert_all():
    insert_usuario()
    insert_pelicula()
    idUsuario = int(get_random_usuario_id())
    idPelicula = int(get_random_pelicula_id())
    if idPelicula is not None and idUsuario is not None:
        insert_renta(idUsuario,idPelicula)


def insert_usuario():
    with connection.cursor() as cursor:
        nombre = fake.name()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        email = fake.email()
        profilePicture = fake.image_url()
        superUser = rd.choice(['0','1'])
        apPat = fake.last_name()
        apMat = fake.last_name()

        sql  = "INSERT INTO `usuarios` (`nombre`, `password`, `email`, `profilePicture`, `superUser`, `apPat`, `apMat`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, password, email,profilePicture,superUser, apPat, apMat ))
        connection.commit()
        print("Se ha agregado un registro a la tabla Usuario")


def insert_pelicula():
    with connection.cursor() as cursor:
        nombre = fake.name()
        genero = fake.random_element(elements=('Drama', 'Comedia', 'Acción', 'Ciencia Ficción', 'Romance'))
        duracion = rd.randint(60,180)
        inventario = rd.randint(1,50)

        sql = "INSERT INTO `peliculas` (`nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, genero, duracion, inventario))
        connection.commit()
        print("Se ha agregado un registro a la tabla Pelicula")




def insert_renta(idUsuario, idPelicula):
    with connection.cursor() as cursor:

        fecha_renta = fake.date_this_year()
        dias_de_renta = rd.randint(1,14)
        estatus = rd.choice([0,1])

        sql = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta,estatus))
        connection.commit()
        print("Se ha agregado un registro a la tabla Rentar")


def get_random_usuario_id():
    with connection.cursor() as cursor:
        cursor.execute("SELECT idUsuario FROM usuarios ORDER BY RAND() LIMIT 1;")
        result = cursor.fetchone()
        if result:
            return result['idUsuario']
        else:                
            return None

def get_random_pelicula_id():
    with connection.cursor() as cursor:
        cursor.execute("SELECT idPelicula FROM peliculas ORDER BY RAND() LIMIT 1;")
        result = cursor.fetchone()
        if result:
            return result['idPelicula']
        else:
            return None

def filter_usuarios_by_lastname_end(substring):
    with connection.cursor() as cursor:
        # Crear patrón de búsqueda para que coincida con el final de los apellidos
        like_pattern = "%" + substring
        # Consulta SQL que busca en ambos campos, apellido paterno y materno
        sql = """
            SELECT * FROM usuarios 
            WHERE apPat LIKE %s 
            OR apMat LIKE %s;
        """
        cursor.execute(sql, (like_pattern, like_pattern))
        results = cursor.fetchall()

        if results:
            print(f"Usuarios encontrados con '{substring}' al final del apellido:")
            for result in results:
                print(result)
        else:
            print("No se encontraron usuarios con esa coincidencia.")

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):

    generos_permitidos = ('Drama', 'Comedia', 'Acción', 'Ciencia Ficción', 'Romance')
    if nuevo_genero not in generos_permitidos:
        print(f"El género '{nuevo_genero}' no es válido. Los géneros permitidos son: {generos_permitidos}")
        return
    with connection.cursor() as cursor:
        # Actualizar el género de la película basado en su nombre
        sql = "UPDATE `peliculas` SET `genero` = %s WHERE `nombre` = %s"
        cursor.execute(sql, (nuevo_genero, nombre_pelicula))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"El género de la película '{nombre_pelicula}' ha sido actualizado a '{nuevo_genero}'.")
        else:
            print(f"No se encontró la película con nombre '{nombre_pelicula}' para actualizar.")

def eliminar_rentas_antiguas():
    with connection.cursor() as cursor:
        # Calcular la fecha límite (hace 3 días desde hoy)
        sql = "DELETE FROM rentar WHERE fecha_renta < DATE_SUB(NOW(), INTERVAL 3 DAY);"
        cursor.execute(sql)
        connection.commit()
        print(f"Se han eliminado las rentas anteriores a 3 días. Total de filas afectadas: {cursor.rowcount}")


#Registros creados para probar todas las funcionalidades
n = 0
while n < 10:
    insert_all()
    n=n+1




