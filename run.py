from flask import Flask,render_template, request
from utils.auth import login_required

from dotenv import load_dotenv
import os
from database import db
from datetime import date

from controllers import usuario_controller, paciente_controller, medico_controller, consulta_medica_controller, login_controller

from seed import seed_data

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(login_controller.auth_bp)

app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(consulta_medica_controller.consulta_medica_bp)

# CONTEXT PROCESSOR
@app.context_processor
def inject_active_path():
    def is_active(path):
        if path == '/':
            if request.path == '/':
                return 'nav-item-active bg-surface-700 text-white'
            return 'text-slate-300 hover:text-white hover:bg-surface-700'
        if request.path.startswith(path):
            return 'nav-item-active bg-surface-700 text-white'
        return 'text-slate-300 hover:text-white hover:bg-surface-700'
    return dict(is_active=is_active)



from models.paciente_model import Paciente
from models.medico_model import Medico
from models.consulta_medica_model import Consulta_Medica
from models.usuario_model import Usuario

@app.route('/')
@login_required
def inicio():

    total_pacientes = Paciente.query.count()
    total_medicos = Medico.query.count()
    total_usuarios = Usuario.query.count()

    consultas_hoy = Consulta_Medica.query.filter(
        db.func.date(Consulta_Medica.fecha) == date.today()
    ).count()

    consultas_recientes = (
        Consulta_Medica.query
        .order_by(Consulta_Medica.fecha.desc())
        .limit(5)
        .all()
    )

    return render_template(
        'dashboard.html',
        total_pacientes=total_pacientes,
        total_medicos=total_medicos,
        total_usuarios=total_usuarios,
        consultas_hoy=consultas_hoy,
        consultas_recientes=consultas_recientes
    )

with app.app_context():
    db.create_all()
    seed_data()
    
if __name__ == '__main__':
    app.run(debug=True)