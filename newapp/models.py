from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(slef):
        return '<Role %r>' % slef.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    factoryID = db.Column(db.String(128), db.ForeignKey('factory.id'))
    EqpID = db.Column(db.String(128))
    # 授权列，暂时不用
    confirmed = db.Column(db.Boolean, default=False)

    # 新增密码散列化
    @property
    def password(self):
        raise AttributeError('password is not a readable attr')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(slef):
        return '<User %r>' % slef.username