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
            Usuario("jrodriguez", "1234", "medico"),
            Usuario("amartinez", "1234", "medico"),
            Usuario("recepcion01", "1234", "enfermero"),
        ]

        db.session.add_all(usuarios)

        print("Usuarios demo creados")

    # =========================
    # MEDICOS DEMO
    # =========================
    if Medico.query.count() == 0:

        medicos = [

            Medico(
                nombre="Dr. Javier Rodriguez",
                especialidad="Cardiologia",
                telefono=70123456,
                correo="jrodriguez@clinicavida.com"
            ),

            Medico(
                nombre="Dra. Andrea Martinez",
                especialidad="Pediatria",
                telefono=71234567,
                correo="amartinez@clinicavida.com"
            ),

            Medico(
                nombre="Dr. Ricardo Salazar",
                especialidad="Traumatologia",
                telefono=72345678,
                correo="rsalazar@clinicavida.com"
            ),

            Medico(
                nombre="Dra. Sofia Quiroga",
                especialidad="Dermatologia",
                telefono=73456789,
                correo="squiroga@clinicavida.com"
            ),

            Medico(
                nombre="Dr. Marcelo Vargas",
                especialidad="Neurologia",
                telefono=74567890,
                correo="mvargas@clinicavida.com"
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
                nombre="Alejandro Fernandez",
                edad="34",
                direccion="Calacoto",
                telefono=61122334
            ),

            Paciente(
                nombre="Camila Gutierrez",
                edad="27",
                direccion="Achumani",
                telefono=62233445
            ),

            Paciente(
                nombre="Roberto Flores",
                edad="45",
                direccion="Sopocachi",
                telefono=63344556
            ),

            Paciente(
                nombre="Valentina Rojas",
                edad="21",
                direccion="Miraflores",
                telefono=64455667
            ),

            Paciente(
                nombre="Fernando Aguilar",
                edad="58",
                direccion="San Miguel",
                telefono=65566778
            ),

            Paciente(
                nombre="Paola Mendoza",
                edad="39",
                direccion="Obrajes",
                telefono=66677889
            ),

            Paciente(
                nombre="Miguel Castro",
                edad="49",
                direccion="Següencoma",
                telefono=67788990
            ),

            Paciente(
                nombre="Luciana Herrera",
                edad="31",
                direccion="Centro",
                telefono=68899001
            ),
        ]

        db.session.add_all(pacientes)

        print("Pacientes demo creados")

    db.session.commit()

    # =========================
    # CONSULTAS MEDICAS DEMO
    # =========================
    if Consulta_Medica.query.count() == 0:

        consultas = [

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=1),
            diagnostico="""
Paciente masculino de 34 años con cefalea, mareos y presión arterial elevada.
Antecedentes familiares de hipertensión y sobrepeso.
Diagnóstico compatible con hipertensión arterial estadio I.
            """,
            tratamiento="""
Losartan 50 mg cada 24 horas.
Reducir consumo de sal y realizar actividad física regular.
Control cardiológico en 30 días.
            """,
            id_medico=1,
            id_paciente=1
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=3),
            diagnostico="""
Paciente femenina de 27 años con fiebre, dolor de garganta y congestión nasal.
Se observan amígdalas inflamadas con exudado.
Diagnóstico de faringoamigdalitis bacteriana aguda.
            """,
            tratamiento="""
Amoxicilina 500 mg cada 8 horas por 7 días.
Paracetamol en caso de fiebre y reposo relativo.
            """,
            id_medico=2,
            id_paciente=2
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=5),
            diagnostico="""
Paciente masculino de 45 años con dolor lumbar posterior a esfuerzo físico.
No presenta signos neurológicos ni limitación motora severa.
Diagnóstico de lumbalgia mecánica aguda.
            """,
            tratamiento="""
Ibuprofeno 400 mg cada 8 horas por 5 días.
Aplicación de calor local y ejercicios lumbares.
Derivación a fisioterapia.
            """,
            id_medico=3,
            id_paciente=3
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=7),
            diagnostico="""
Paciente femenina de 21 años con lesiones pruriginosas en brazos y cuello.
Antecedente de uso reciente de productos cosméticos.
Diagnóstico de dermatitis alérgica de contacto.
            """,
            tratamiento="""
Crema de hidrocortisona al 1% dos veces al día.
Antihistamínico oral en caso de prurito.
Suspender producto sospechoso.
            """,
            id_medico=4,
            id_paciente=4
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=10),
            diagnostico="""
Paciente masculino de 58 años con migraña recurrente y fotofobia.
Refiere aumento de frecuencia de episodios en el último mes.
Diagnóstico de migraña crónica sin aura.
            """,
            tratamiento="""
Sumatriptán 50 mg al inicio de cada episodio.
Registro de frecuencia e intensidad de cefaleas.
Control neurológico en 30 días.
            """,
            id_medico=5,
            id_paciente=5
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=2),
            diagnostico="""
Control médico preventivo con revisión general de salud.
No se identifican alteraciones clínicas significativas.
Estado general satisfactorio.
            """,
            tratamiento="""
Mantener alimentación equilibrada y actividad física regular.
Control preventivo anual.
            """,
            id_medico=2,
            id_paciente=6
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=12),
            diagnostico="""
Paciente masculino de 49 años con dolor torácico durante esfuerzos moderados.
Presenta antecedentes de obesidad e hipercolesterolemia.
Sospecha de enfermedad coronaria estable.
            """,
            tratamiento="""
Solicitud de prueba de esfuerzo y perfil lipídico.
Aspirina 100 mg diaria bajo supervisión médica.
Control cardiológico especializado.
            """,
            id_medico=1,
            id_paciente=7
        ),

        Consulta_Medica(
            fecha=datetime.now() - timedelta(days=15),
            diagnostico="""
Paciente femenina de 31 años con hormigueo en manos y fatiga frecuente.
Examen neurológico inicial sin alteraciones importantes.
Se solicitan estudios complementarios.
            """,
            tratamiento="""
Complejo vitamínico B durante 30 días.
Solicitar hemograma y vitamina B12.
Seguimiento neurológico posterior.
            """,
            id_medico=5,
            id_paciente=8
        ),
    ]

        db.session.add_all(consultas)

        print("Consultas demo creadas")

    db.session.commit()

    print("Base de datos inicializada correctamente")