from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from models.usuario_model import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = Usuario.get_by_username(username)

        if user and user.check_password(password):

            session['user_id'] = user.id_usuario
            session['username'] = user.username
            session['rol'] = user.rol

            flash('Bienvenido', 'success')

            return redirect(url_for('dashboard.inicio'))

        flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():

    session.clear()

    flash('Sesión cerrada', 'info')

    return redirect(url_for('auth.login'))