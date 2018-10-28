from flask import jsonify, request
from app.users.model import Users
from app.auth.auths import Auth
from .. import common
import logging
import json

def init_api(app):
    @app.route('/register', methods=['POST'])
    def register():
        """
        用户注册
        :return: json
        """
        # if request.data:
        #     data = request.data
        #     logging.error(type(data))
        #     dataDict = json.loads(data)
        #     logging.error(dataDict)
        data = request.data
        dataDict = json.loads(data)

        email = dataDict.get('email',None)
        username = dataDict.get('username',None)
        password = dataDict.get('password',None)
        # 最后一条记录及其ID
        lastUserRecord = Users.query.order_by('-id').first()
        if (lastUserRecord is None):
            newRecordId = 1
        else:
            newRecordId = lastUserRecord.id + 1
        user = Users(id=newRecordId, email=email, username=username, password=Users.set_password(Users, password))
        reason = Users.add(Users, user) ## unique constraint failed
        userInfo = Users.get(Users, user.id)
        if userInfo:
            returnUser = {
                'id': userInfo.id,
                'username': userInfo.username,
                'email': userInfo.email,
                'login_time': userInfo.login_time
            }
            return jsonify(common.trueReturn(returnUser, "用户注册成功"))
        else:
            return jsonify(common.falseReturn('', '用户注册失败'))


    @app.route('/login', methods=['POST'])
    def login():
        """
        用户登录
        :return: json
        """
        if not request.data:
            return jsonify(common.falseReturn('', 'post 数据为空'))
        data = request.data
        # data_str = data.decode('utf-8')
        data_dict = json.loads(data)
        username = data_dict.get('username',None)
        password = data_dict.get('password',None)
        if (not username or not password):
            return jsonify(common.falseReturn('', '用户名和密码不能为空'))
        else:
            return Auth.authenticate(Auth, username, password)


    @app.route('/user', methods=['GET'])
    def get():
        """
        获取用户信息
        :return: json
        """
        result ,expiretime = Auth.identify(Auth, request)
        if (result['status'] and result['data']):
            user = Users.get(Users, result['data'])
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time,
                '过期时间': expiretime
            }
            result = common.trueReturn(returnUser, "请求成功")
        return jsonify(result)