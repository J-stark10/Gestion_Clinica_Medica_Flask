from flask import Flask, request

from database import db
from seed import seed_data

from dotenv import load_dotenv
import os

from controllers import login_controller, dashboard_controller, usuario_controller, paciente_controller, medico_controller, consulta_medica_controller

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(login_controller.auth_bp)

app.register_blueprint(dashboard_controller.dashboard_bp)
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

with app.app_context():
    db.create_all()
    seed_data()
    
if __name__ == '__main__':
    app.run(debug=True)