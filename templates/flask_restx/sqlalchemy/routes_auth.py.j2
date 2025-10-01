# templates/flask_restx/sqlalchemy/routes_auth.py.j2
"""
API routes with authentication
"""
from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from src.models.models import User
from src.extensions import db, api

# Authorization configuration
authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer {token}"'
    }
}

user_ns = Namespace(
    'auth',
    description='Authentication operations',
    authorizations=authorizations
)

# API Models for request/response documentation
register_model = user_ns.model('Register', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password'),
})

login_model = user_ns.model('Login', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
})

user_model = user_ns.model('User', {
    'id': fields.Integer(description='User ID'),
    'username': fields.String(description='Username'),
    'email': fields.String(description='Email address'),
})


@user_ns.route('/register')
class Register(Resource):
    """User registration"""

    @user_ns.expect(register_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Register a new user"""
        data = request.json

        # Validate input
        if not all(k in data for k in ('username', 'email', 'password')):
            user_ns.abort(400, 'Missing required fields')

        # Check if user exists
        if User.query.filter_by(username=data['username']).first():
            user_ns.abort(400, 'Username already exists')

        if User.query.filter_by(email=data['email']).first():
            user_ns.abort(400, 'Email already exists')

        # Create user
        user = User(
            username=data['username'],
            email=data['email']
        )
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()

        return user, 201


@user_ns.route('/login')
class Login(Resource):
    """User login"""

    @user_ns.expect(login_model)
    def post(self):
        """Login and get access token"""
        data = request.json

        user = User.query.filter_by(username=data.get('username')).first()

        if not user or not user.check_password(data.get('password')):
            user_ns.abort(401, 'Invalid credentials')

        access_token = create_access_token(identity=user)

        return {
            'access_token': access_token,
            'user': user.to_dict()
        }, 200


@user_ns.route('/me')
class CurrentUser(Resource):
    """Current user operations"""

    @user_ns.doc(security='Bearer')
    @jwt_required()
    @user_ns.marshal_with(user_model)
    def get(self):
        """Get current user info"""
        current_user = get_jwt_identity()
        user = User.query.get(current_user)

        if not user:
            user_ns.abort(404, 'User not found')

        return user


@user_ns.route('/users')
class UserList(Resource):
    """User list operations"""

    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        users = User.query.all()
        return users