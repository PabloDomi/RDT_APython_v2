# templates/flask_restx/sqlalchemy/models.py.j2
"""
Database models
"""
from src.extensions import db
from src.security import PasswordValidator


class User(db.Model):
    """User model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password: str):
        """Hash and set password"""
        self.password_hash = PasswordValidator.hash_password(password)
    
    def check_password(self, password: str) -> bool:
        """Verify password against hash"""
        return PasswordValidator.verify_password(password, self.password_hash)

    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }