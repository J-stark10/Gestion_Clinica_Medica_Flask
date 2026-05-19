from database import db

class Consulta_Medica(db.Model):
    __tablename__ = 'consultas_medicas'

    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    diagnostico = db.Column(db.String(200), nullable=False)
    tratamiento = db.Column(db.String(100), nullable=False)

    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'))

    medico = db.relationship('Medico', back_populates='consultas_medicas')
    paciente = db.relationship('Paciente', back_populates='consultas_medicas')

    def __init__(self, fecha, diagnostico, tratamiento, id_medico, id_paciente):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.id_medico = id_medico
        self.id_paciente = id_paciente

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Consulta_Medica.query.all()

    @staticmethod
    def get_by_id(id_consulta):
        return Consulta_Medica.query.get(id_consulta)

    def update(self, fecha, diagnostico , tratamiento, id_medico, id_paciente):
        if fecha and diagnostico and tratamiento and id_medico and id_paciente:
            self.fecha = fecha
            self.diagnostico = diagnostico
            self.tratamiento = tratamiento
            self.id_medico = id_medico
            self.id_paciente = id_paciente
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

    @staticmethod
    def get_by_paciente(id_paciente):
        return Consulta_Medica.query.filter_by(id_paciente=id_paciente).all()