from flask import request, redirect, url_for, Blueprint 
from sqlalchemy import func

from utils.auth import login_required
from datetime import datetime

from models.consulta_medica_model import Consulta_Medica
from views import consulta_medica_view

from models.medico_model import Medico
from models.paciente_model import Paciente

consulta_medica_bp = Blueprint('consulta_medica', __name__, url_prefix='/consultas_medicas')

@consulta_medica_bp.route('/')
@login_required
def index():
    fecha = request.args.get('fecha')
    if fecha:
        consultas_medicas = Consulta_Medica.query.filter(
            func.date(Consulta_Medica.fecha) == fecha
        ).all()
    else:
        consultas_medicas = Consulta_Medica.get_all()
    return consulta_medica_view.list(consultas_medicas)

@consulta_medica_bp.route('/create', methods=['GET','POST'])
@login_required
def create():
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta_medica = Consulta_Medica(fecha, diagnostico, tratamiento, id_medico, id_paciente)
        consulta_medica.save()

        return redirect(url_for('consulta_medica.index'))
    
    return consulta_medica_view.create(medicos, pacientes)

@consulta_medica_bp.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    consulta_medica = Consulta_Medica.get_by_id(id)

    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta_medica.update(fecha, diagnostico, tratamiento, id_medico, id_paciente)
        return redirect(url_for('consulta_medica.index'))

    return consulta_medica_view.edit(consulta_medica, medicos, pacientes)

@consulta_medica_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    consulta_medica = Consulta_Medica.get_by_id(id)
    consulta_medica.delete()

    return redirect(url_for('consulta_medica.index'))



