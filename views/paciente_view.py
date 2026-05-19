from flask import render_template

def list(pacientes):
    return render_template('pacientes/index.html', pacientes=pacientes)

def create():
    return render_template('pacientes/create.html')

def edit(paciente):
    return render_template('pacientes/edit.html', paciente=paciente)

def historial(paciente, consultas_medicas):
    return render_template('pacientes/historial.html', paciente=paciente, consultas_medicas=consultas_medicas)