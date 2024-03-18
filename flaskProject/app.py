from flask import Flask, render_template
from alchemyClasses import db
from controllers.controller_usuario import usuario_blueprint
from controllers.controller_pelicula import pelicula_blueprint
from controllers.controller_renta import renta_blueprint


#se cambio la ruta de la base de datos, la contraseña y el nombre de la base de datos
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Develooper123!@localhost:3306/ing_soft'
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software"
)
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(renta_blueprint)

@app.route('/')
def hello_world():
    #cuevana.html esta es el menu principal, de ahi se redigira a las demas paginas
    return render_template('cuevana.html')

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=5000)