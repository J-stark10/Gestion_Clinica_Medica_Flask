from database import db

class Medico(db.Model):
    __tablename__ = 'medicos'

    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(7), nullable=False)
    correo = db.Column(db.String(20), nullable=False)

    consultas_medicas = db.relationship('Consulta_Medica', back_populates='medico')

    def __init__(self, nombre, especialidad, telefono, correo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Medico.query.all()
    
    @staticmethod
    def get_by_id(id_medico):
        return Medico.query.get(id_medico)
    
    def update(self, nombre, especialidad, telefono, correo):
        if nombre and especialidad and telefono and correo:
            self.nombre = nombre
            self.especialidad = especialidad
            self.telefono = telefono
            self.correo = correo
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()