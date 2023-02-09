from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from project import db,login
from datetime import datetime





class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True,nullable=False)
    email = db.Column(db.String(100), index=True, unique=True,nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    #Hashing the password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Checking the hashed  password 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    #Return string message
    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Post(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)  


#Load users id
@login.user_loader
def load_user(id):
    return User.query.get(int(id))      
#  <!-- {% if current_user.is_anonymous %} -->
    #  <!-- {% endif %} -->
    # <!-- {% else %} -->