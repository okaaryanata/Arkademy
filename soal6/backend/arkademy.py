from flask import Flask, request, json, session, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import marshal, fields
from flask_cors import CORS, cross_origin
import os
import requests
from requests.utils import quote
import string

app = Flask(__name__)
# GANTI CONFIG DIBAWAH MENYESUAIKAN USER,PASS,HOST,PORT YANG ANDA GUNAKAN UNTUK POSTGRESQL ANDA
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kumiskucing@localhost:5432/arkademy'
CORS(app, suppor_credentials=True)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


@app.route('/')
def get():
    return"kumiskucing", 201


@app.route('/add-user', methods=['POST'])
def addUser():
    request_data = request.get_json()
    req_username = request_data.get('username')
    if req_username == None:
        return 'Username Kosong',400
    dataUser = Users.query.filter_by(name=req_username).first()
    if dataUser:
        return 'Username telah terdaftar', 400
    else:
        data = Users(
            name=req_username
        )
        db.session.add(data)
        db.session.commit()
        return 'Sukses', 201


@app.route('/add-skill', methods=['POST'])
def addSkill():
    request_data = request.get_json()
    req_user = request_data.get('user_id')
    req_skill = request_data.get('skill')
    user = Users.query.filter_by(id=req_user).first()
    if user:
        skill = Skills.query.filter_by(name=req_skill,user_id=req_user).first()
        if skill:
            return 'Skill sudah terdaftar', 400
        else:
            data = Skills(
                name=req_skill,
                user_id=req_user
            )
            db.session.add(data)
            db.session.commit()
            return 'Sukses tambah skill', 201


@app.route('/get-all-user', methods=['GET'])
def getAllUser():
    userData = Users.query.all()
    arr_user = []
    if userData:
        for user in userData:
            userSkills = Skills.query.filter_by(user_id=user.id).all()
            skills = ""
            for i in range(len(userSkills)):
                if i != len(userSkills)-1:
                    skills += str(userSkills[i].name) + ", "
                else:
                    skills += str(userSkills[i].name)
            json_format = {
                "user_id": user.id,
                "name": user.name,
                "skills": skills
            }
            arr_user.append(json_format)
    user_json = json.dumps(arr_user)
    return user_json, 201


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), host=os.getenv(
        "HOST"), port=os.getenv("PORT"))
