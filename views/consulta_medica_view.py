from flask import render_template

def list(consultas_medicas):
    return render_template('consultas_medicas/index.html', consultas_medicas=consultas_medicas)

def create(medicos, pacientes):
    return render_template('consultas_medicas/create.html', medicos=medicos, pacientes=pacientes)

def edit(consulta_medica, medicos, pacientes):
    return render_template('consultas_medicas/edit.html',consulta_medica=consulta_medica, medicos=medicos, pacientes=pacientes)