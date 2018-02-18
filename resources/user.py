import sqlite3
from flask_restful import Resource,reqparse
from models.usermodel import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field can not be left blank")
    parser.add_argument('password', type=str, required=True, help="This field can not be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_user_byusername(data['username']):
            return {'message' : 'User allready exists'},400

        user = UserModel(**data)
        user.save_to_db()

        return {'message' : 'User create sucessfully'},201

