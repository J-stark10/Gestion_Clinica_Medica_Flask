from database import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.String(2), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(8), nullable=False)

    consultas_medicas = db.relationship('Consulta_Medica', back_populates='paciente')

    def __init__(self, nombre, edad, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()
    
    @staticmethod
    def get_by_id(id_paciente):
        return Paciente.query.get(id_paciente)
    
    def update(self, nombre, edad, direccion, telefono):
        if nombre and edad and direccion and telefono:
            self.nombre = nombre
            self.edad = edad
            self.direccion = direccion
            self.telefono = telefono
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()