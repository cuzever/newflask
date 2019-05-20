from datetime import datetime
from flask import request
from flask_login import current_user
from . import db
from .models import Equipment, FaultMsg, NewVal, stateList, test_water

class Query_now():

    res = {}
    keys = ['Tag1','Tag2','Tag3','Tag4','weight']
    result = db.session.query(NewVal).order_by(NewVal.id.desc()).first()
    
    
    # dicRes = {}
    # date = datetime(2018, 6, 17, 9, 0, 0).strftime('%Y-%m-%d %H:%M:%S')[:10]
    # eqp = request.form.get("eqp", "")
    # NewVal.__table__.name = current_user.factoryID + eqp + 'newval' + date
    # result = db.session.query(NewVal).order_by(NewVal.id.desc()).first()
    # dicRes['Tag1'] = result.WeightTag1
    # dicRes['Tag2'] = result.WeightTag2
    # dicRes['Tag3'] = result.WeightTag3
    # dicRes['Tag4'] = result.WeightTag4
    # dicRes['weight'] = result.WeightTag1 + result.WeightTag2 + result.WeightTag3 + result.WeightTag4
    # FaultMsg.__table__.name = current_user.factoryID + eqp + 'faultmsg' + date
    # result2 = db.session.query(FaultMsg).order_by(FaultMsg.id.desc()).first()
    # Partial = judgeFault(result2.Partial)[1: 5]
    # Forced = judgeFault(result2.Forced)[1: 5]
    # Loss = judgeFault(result2.Loss)[1: 5]
    # Over = judgeFault(result2.Over)[1: 5]