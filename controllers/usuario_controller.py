from flask import session, request, redirect, url_for, Blueprint, flash
from  utils.auth import login_required

from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuario', __name__, url_prefix=('/usuarios'))

@usuario_bp.route('/')
@login_required
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():

    if request.method == 'POST':

        username = request.form['username'].strip()
        password = request.form['password']
        rol = request.form['rol']

        if len(username) < 3:
            flash('El nombre de usuario debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('usuario.create'))

        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return redirect(url_for('usuario.create'))

        usuario_existente = Usuario.get_by_username(username)

        if usuario_existente:
            flash('El nombre de usuario ya existe', 'error')
            return redirect(url_for('usuario.create'))

        usuario = Usuario(username, password, rol)
        usuario.save()

        flash('Usuario creado correctamente', 'success')
        return redirect(url_for('usuario.index'))

    return usuario_view.create()

@usuario_bp.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    usuario = Usuario.get_by_id(id)

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        rol = request.form['rol']
    
        usuario_existente = Usuario.get_by_username(username)
        if usuario_existente and usuario_existente.id_usuario != usuario.id_usuario:
            flash('El nombre de usuario ya existe', 'error')
            return redirect(url_for('usuario.edit', id=id))
        
        if len(username) < 3:
            flash('El nombre de usuario debe tener al menos 3 caracteres', 'error')
            return redirect(url_for('usuario.edit', id=id))

        if  password and len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return redirect(url_for('usuario.edit', id=id))

        usuario.update(username, password, rol)
        
        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('usuario.index'))

    return usuario_view.edit(usuario)

@usuario_bp.route('/delete/<int:id>')
@login_required
def delete(id):

    if session.get('user_id') == id:
        flash('No puedes eliminar tu propio usuario mientras tienes la sesión activa', 'error')
        return redirect(url_for('usuario.index'))

    usuario = Usuario.get_by_id(id)
    usuario.delete()

    flash('Usuario eliminado correctamente', 'success')
    
    return redirect(url_for('usuario.index'))


@usuario_bp.route('/search')
@login_required
def search():
    search = request.args.get('search', '').strip()
    if search:
        usuarios = Usuario.search(search)
    else: 
        usuarios = Usuario.get_all()
    
    return usuario_view.list(usuarios)
    