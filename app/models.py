from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
import datetime


#加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    EqpID = db.Column(db.String(128))
    factoryID = db.Column(db.String(128), db.ForeignKey('factory.id'))
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


#设备表
class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer,primary_key=True)
    fid = db.Column(db.String(20))
    eid = db.Column(db.String(20))
    place = db.Column(db.String(20), index=True)
    supplier = db.Column(db.String(20))
    spl_address = db.Column(db.String(100))
    spl_contact = db.Column(db.String(20))
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    SencerNum = db.Column(db.Integer)
    SencerName = db.Column(db.String(125))
    NoLoad_set = db.Column(db.String(100))
    EmptyLoad_set = db.Column(db.String(100))
    Temp = db.Column(db.Float)
    Wet = db.Column(db.Float)
    ExcV = db.Column(db.Float)
    Sensitivity = db.Column(db.Float)
    Resistance = db.Column(db.Integer)
    Thread = db.relationship('Thread',backref='Eqp')
    stateList = db.relationship('stateList',backref='Eqp')
    NewVal = db.relationship('NewVal',backref='Eqp')
    FaultMsg = db.relationship('FaultMsg',backref='Eqp')
    __table_args__ = (
        db.UniqueConstraint('fid', 'eid', name='uix_fid_eid'),#联合唯一索引
    )

class Thread(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True)
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    standard = db.Column(db.Float)
    zeropoint = db.Column(db.Float)
    Eid = db.Column(db.Integer,db.ForeignKey('equipment.id'))

class stateList(db.Model):
    __tablename__ = 'statelist'
    id = db.Column(db.Integer, primary_key=True)
    FaultTime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    RecoverTime = db.Column(db.DateTime)
    PeriodSecond = db.Column(db.Integer)
    FaultSencer = db.Column(db.String(20), index=True)
    FaultCode = db.Column(db.Integer, index=True)
    FaultState = db.Column(db.Boolean)
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    record = db.Column(db.String(250))
    Eid = db.Column(db.Integer,db.ForeignKey('equipment.id'))

class NewVal(db.Model):
    __tablename__ = 'newval'
    id = db.Column(db.Integer, primary_key=True)
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    WeightTag1 = db.Column(db.Float)
    WeightTag2 = db.Column(db.Float)
    WeightTag3 = db.Column(db.Float)
    WeightTag4 = db.Column(db.Float)
    Weight = db.Column(db.Float)
    Eid = db.Column(db.Integer,db.ForeignKey('equipment.id'))

class FaultMsg(db.Model):
    __tablename__ = 'faultmsg'
    id = db.Column(db.Integer, primary_key=True)
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    Partial = db.Column(db.Integer)
    Forced = db.Column(db.Integer)
    Loss = db.Column(db.Integer)
    Over = db.Column(db.Integer)
    eqpState = db.Column(db.Integer)
    Eid = db.Column(db.Integer,db.ForeignKey('equipment.id'))

class test_water(db.Model):
    __tablename__ = 'scale_PredWaterData'
    __bind_key__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    Timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    WeightTag1 = db.Column(db.Float)
    WeightTag2 = db.Column(db.Float)
    WeightTag3 = db.Column(db.Float)
    WeightTag4 = db.Column(db.Float)
    Weight = db.Column(db.Float)
    PredW1 = db.Column(db.Float)
    PredW2 = db.Column(db.Float)
    PredW3 = db.Column(db.Float)
    PredW4 = db.Column(db.Float)
    PredW = db.Column(db.Float)
    PartialLoadFlag = db.Column(db.Integer)
    SensorTag1 = db.Column(db.Integer)
    SensorTag2 = db.Column(db.Integer)
    SensorTag3 = db.Column(db.Integer)
    SensorTag4 = db.Column(db.Integer)
    EQP_State = db.Column(db.Integer)
    Normal = db.Column(db.Integer)
    AlertF = db.Column(db.Integer)
    AlarmF = db.Column(db.Integer)