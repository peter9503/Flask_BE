from main import app
from main import db
from flask_jwt_extended import verify_jwt_in_request, create_access_token
from flask import request
from model.account import account

import json

@app.route("/create_db", methods=['POST'])
def create_db():
    db.create_all()
    return "good"

@app.route('/account/login', methods=['POST'])
def account_login():
    out = { "state"     :"1",
            "gwt_token" :"" ,
            "msg"       :""  }
    try:
        js_data = json.loads(request.data.decode('ascii'))
    except:
        js_data = request.form

    if len(js_data) == 0:
        out["state"] = 0
        out["msg"]   = "not a json string data"
    
    elif "account" not in js_data or "password" not in js_data:
        out["state"] = 0
        out["msg"]   = "do not receive account or password"

    else:
        q = account.query.filter_by(account = js_data["account"]).first()
        if q is None:
            out["state"] = 0
            out["msg"]   = "account doesn't exist"

        elif not q.valid_password(js_data["password"]):
            out["state"] = 0
            out["msg"]   = "wrong password"            
        
        else:
            if js_data["account"] == 'admin':
                out["jwt_token"] = create_access_token(identity="admin")
            else:
                out["jwt_token"] = create_access_token(identity="normal")

    return json.dumps(out)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)