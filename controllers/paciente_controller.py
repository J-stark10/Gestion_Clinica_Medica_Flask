from flask import flash,request, redirect, url_for, Blueprint
from utils.auth import login_required

from models.paciente_model import Paciente
from models.consulta_medica_model import Consulta_Medica
from views import paciente_view

paciente_bp = Blueprint('paciente', __name__, url_prefix=('/pacientes'))

@paciente_bp.route('/')
@login_required
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route('/create', methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        if len(nombre) < 3: 
            flash('El nombre debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('paciente.create'))
        
        paciente = Paciente(nombre, edad, direccion, telefono)
        paciente.save()

        flash('Paciente creado exitosamente', 'success')
        return redirect(url_for('paciente.index'))
    return paciente_view.create()

@paciente_bp.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    paciente = Paciente.get_by_id(id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        if len(nombre) < 3:
            flash('El nombre debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('paciente.edit', id=id))

        paciente.update(nombre, edad, direccion, telefono)
        flash('Paciente actualizado exitosamente', 'success')
        return redirect(url_for('paciente.index'))
    return paciente_view.edit(paciente)

@paciente_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()

    flash('Paciente eliminado exitosamente', 'success')
    return redirect(url_for('paciente.index'))

@paciente_bp.route('/historial/<int:id>')
@login_required
def historial(id):

    paciente = Paciente.get_by_id(id)
    consultas_medicas = Consulta_Medica.get_by_paciente(id)

    return paciente_view.historial(paciente, consultas_medicas)