from database import db

from models.usuario_model import Usuario
from models.medico_model import Medico
from models.paciente_model import Paciente
from models.consulta_medica_model import Consulta_Medica

from datetime import datetime, timedelta


def seed_data():

    # =========================
    # USUARIOS DEMO
    # =========================
    if Usuario.query.count() == 0:

        usuarios = [
            Usuario("admin", "1234", "administrador"),
            Usuario("doctor1", "1234", "medico"),
            Usuario("doctor2", "1234", "medico"),
            Usuario("recepcion", "1234", "enfermero"),
        ]

        db.session.add_all(usuarios)

        print("Usuarios demo creados")

    # =========================
    # MEDICOS DEMO
    # =========================
    if Medico.query.count() == 0:

        medicos = [

            Medico(
                nombre="Carlos Mendoza",
                especialidad="Cardiologia",
                telefono="7123456",
                correo="cmendoza@clinica.com"
            ),

            Medico(
                nombre="Ana Lopez",
                especialidad="Pediatria",
                telefono="7234567",
                correo="alopez@clinica.com"
            ),

            Medico(
                nombre="Luis Fernandez",
                especialidad="Traumatologia",
                telefono="7345678",
                correo="lfernandez@clinica.com"
            ),

            Medico(
                nombre="Gabriela Rojas",
                especialidad="Dermatologia",
                telefono="7456789",
                correo="grojas@clinica.com"
            ),

            Medico(
                nombre="Miguel Vargas",
                especialidad="Neurologia",
                telefono="7567890",
                correo="mvargas@clinica.com"
            ),
        ]

        db.session.add_all(medicos)

        print("Medicos demo creados")

    # =========================
    # PACIENTES DEMO
    # =========================
    if Paciente.query.count() == 0:

        pacientes = [

            Paciente(
                nombre="Juan Perez",
                edad="30",
                direccion="Zona Sur",
                telefono="6111111"
            ),

            Paciente(
                nombre="Maria Gomez",
                edad="25",
                direccion="Miraflores",
                telefono="6222222"
            ),

            Paciente(
                nombre="Ricardo Flores",
                edad="41",
                direccion="Sopocachi",
                telefono="6333333"
            ),

            Paciente(
                nombre="Daniela Ruiz",
                edad="19",
                direccion="Obrajes",
                telefono="6444444"
            ),

            Paciente(
                nombre="Fernando Castillo",
                edad="52",
                direccion="Calacoto",
                telefono="6555555"
            ),

            Paciente(
                nombre="Lucia Herrera",
                edad="36",
                direccion="Achumani",
                telefono="6666666"
            ),

            Paciente(
                nombre="Marco Alvarez",
                edad="47",
                direccion="San Miguel",
                telefono="6777777"
            ),

            Paciente(
                nombre="Valeria Molina",
                edad="28",
                direccion="Centro",
                telefono="6888888"
            ),
        ]

        db.session.add_all(pacientes)

        print("Pacientes demo creados")

    db.session.commit()

    # =========================
    # CONSULTAS DEMO
    # =========================
    if Consulta_Medica.query.count() == 0:

        consultas = [

            Consulta_Medica(
                fecha=datetime.now() - timedelta(days=1),
                diagnostico="Hipertension arterial",
                tratamiento="Losartan 50mg",
                id_medico=1,
                id_paciente=1
            ),

            Consulta_Medica(
                fecha=datetime.now() - timedelta(days=2),
                diagnostico="Infeccion respiratoria",
                tratamiento="Amoxicilina",
                id_medico=2,
                id_paciente=2
            ),

            Consulta_Medica(
                fecha=datetime.now() - timedelta(days=3),
                diagnostico="Dermatitis alergica",
                tratamiento="Crema con hidrocortisona",
                id_medico=4,
                id_paciente=4
            ),

            Consulta_Medica(
                fecha=datetime.now() - timedelta(days=4),
                diagnostico="Dolor lumbar",
                tratamiento="Ibuprofeno y fisioterapia",
                id_medico=3,
                id_paciente=3
            ),

            Consulta_Medica(
                fecha=datetime.now() - timedelta(days=5),
                diagnostico="Migraña cronica",
                tratamiento="Sumatriptan",
                id_medico=5,
                id_paciente=5
            ),

            Consulta_Medica(
                fecha=datetime.now(),
                diagnostico="Control pediatrico",
                tratamiento="Vitaminas y seguimiento",
                id_medico=2,
                id_paciente=6
            ),
        ]

        db.session.add_all(consultas)

        print("Consultas demo creadas")

    db.session.commit()

    print("Base de datos inicializada correctamente")