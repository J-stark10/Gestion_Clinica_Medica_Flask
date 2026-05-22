from database import db

from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    rol = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, rol):
        self.username = username
        self.password = self.has_password(password)
        self.rol = rol
    
    @staticmethod
    def has_password(password):
        return generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id_user):
        return Usuario.query.get(id_user)
    
    def update(self, username, password, rol):
        self.username = username
        self.rol = rol
        
        if password:
            self.password = self.has_password(password)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()
    
    @staticmethod
    def search(search):
        return Usuario.query.filter(Usuario.username.ilike(f'%{search}%')).all()

    
