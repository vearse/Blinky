from turtle import title
from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .. import db



class Podcaster(db.Model):
    __tablename__ = 'playpodcaster'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    code = db.Column(db.String(64),  unique=True, index=True)
    language = db.Column(db.String(64))
    speaker = db.Column(db.String(64))
    title = db.Column(db.String(64))
    status = db.Column(db.String(64))
    content = db.Column(db.Text)
    podcast = db.Column(db.String(128))
    videography = db.Column(db.String(128))
    extra = db.Column(db.String(64))
    created_at = db.Column(db.Date())

    # def __init__(self, **kwargs):
    #     super(Podcaster, self).__init__(**kwargs)

 
#     @property
#     def password(self):
#         raise AttributeError('`password` is not a readable attribute')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def generate_confirmation_token(self, expiration=604800):
#         """Generate a confirmation token to email a new user."""

#         s = Serializer(current_app.config['SECRET_KEY'], expiration)
#         return s.dumps({'confirm': self.id})

#     def generate_email_change_token(self, new_email, expiration=3600):
#         """Generate an email change token to email an existing user."""
#         s = Serializer(current_app.config['SECRET_KEY'], expiration)
#         return s.dumps({'change_email': self.id, 'new_email': new_email})

#     def generate_password_reset_token(self, expiration=3600):
#         """
#         Generate a password reset change token to email to an existing user.
#         """
#         s = Serializer(current_app.config['SECRET_KEY'], expiration)
#         return s.dumps({'reset': self.id})

#     def confirm_account(self, token):
#         """Verify that the provided token is for this user's id."""
#         s = Serializer(current_app.config['SECRET_KEY'])
#         try:
#             data = s.loads(token)
#         except (BadSignature, SignatureExpired):
#             return False
#         if data.get('confirm') != self.id:
#             return False
#         self.confirmed = True
#         db.session.add(self)
#         db.session.commit()
#         return True

#     def change_email(self, token):
#         """Verify the new email for this user."""
#         s = Serializer(current_app.config['SECRET_KEY'])
#         try:
#             data = s.loads(token)
#         except (BadSignature, SignatureExpired):
#             return False
#         if data.get('change_email') != self.id:
#             return False
#         new_email = data.get('new_email')
#         if new_email is None:
#             return False
#         if self.query.filter_by(email=new_email).first() is not None:
#             return False
#         self.email = new_email
#         db.session.add(self)
#         db.session.commit()
#         return True

#     def reset_password(self, token, new_password):
#         """Verify the new password for this user."""
#         s = Serializer(current_app.config['SECRET_KEY'])
#         try:
#             data = s.loads(token)
#         except (BadSignature, SignatureExpired):
#             return False
#         if data.get('reset') != self.id:
#             return False
#         self.password = new_password
#         db.session.add(self)
#         db.session.commit()
#         return True

#     @staticmethod
#     def generate_fake(count=100, **kwargs):
#         """Generate a number of fake users for testing."""
#         from sqlalchemy.exc import IntegrityError
#         from random import seed, choice
#         from faker import Faker

#         fake = Faker()
#         roles = Role.query.all()

#         print(roles)
#         seed()
#         for i in range(count):
#             u = User(
#                 first_name=fake.first_name(),
#                 last_name=fake.last_name(),
#                 email=fake.email(),
#                 password='password',
#                 confirmed=True,
#                 role=choice(roles),
#                 **kwargs)
#             db.session.add(u)
#             try:
#                 db.session.commit()
#             except IntegrityError:
#                 db.session.rollback()

#     def __repr__(self):
#         return '<User \'%s\'>' % self.full_name()


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
