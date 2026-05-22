from flask import flash, request, redirect, url_for, Blueprint
from utils.auth import login_required

from models.medico_model import Medico
from views import medico_view

medico_bp = Blueprint('medico', __name__, url_prefix=('/medicos'))

@medico_bp.route('/')
@login_required
def index():
    medicos = Medico.get_all()
    return medico_view.list(medicos)

@medico_bp.route('/create', methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        if len(nombre) < 3:
            flash('El nombre debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('medico.create'))

        if len(especialidad) < 3:
            flash('La especialidad debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('medico.create'))

        medico = Medico(nombre, especialidad, telefono, correo)
        medico.save()

        flash('Médico creado exitosamente', 'success')
        return redirect(url_for('medico.index'))
    
    return medico_view.create()

@medico_bp.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    medico = Medico.get_by_id(id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        if len(nombre) < 3:
            flash('El nombre debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('medico.index', id=id))

        if len(especialidad) < 3:
            flash('La especialidad debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('medico.index', id=id))
        
        medico.update(nombre, especialidad, telefono, correo)

        flash('Médico actualizado exitosamente', 'success')
        return redirect(url_for('medico.index'))
    
    return medico_view.edit(medico)

@medico_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    medico = Medico.get_by_id(id)
    medico.delete()

    flash('Médico eliminado exitosamente', 'success')
    return redirect(url_for('medico.index'))
