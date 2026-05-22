from flask import app, render_template, Blueprint
from database import db
from datetime import date

from models.paciente_model import Paciente
from models.medico_model import Medico
from models.consulta_medica_model import Consulta_Medica
from models.usuario_model import Usuario
from utils.auth import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
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