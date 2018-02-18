from werkzeug.security import safe_str_cmp
from models.usermodel import UserModel

def authenticate(username,password):
    user = UserModel.find_user_byusername(username)
    print(user)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return UserModel.find_user_byID(user_id)

