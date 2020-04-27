from flask import request, jsonify, url_for, make_response, redirect
from code import app
import yaml
import base64
from time import time
import traceback

class User(object):
    def __init__(self, data):
        self.data = data

    def get_data(self) -> str:
        for key in self.data.keys():
            if isinstance(self.data[key], bytes):
                self.data[key] = self.data[key].decode()

        return "Nickname: {nickname}\nRole: {role}\nCreated at: {created_at}".format(**self.data)

@app.route('/')
def redirect_to_main():
    resp = make_response(redirect(url_for('user_info')))
    data = yaml.dump({'nickname': 'user', 'role': 'Admin', 'created_at': time()})
    resp.set_cookie('session', base64.b64encode(data.encode()))
    return resp

@app.route('/user/get')
def user_info():
    cookies = request.cookies
    if not cookies:
        return url_for('redirect_to_main')

    try:
        cookies_decoded = base64.b64decode(cookies['session']).decode()
        cookies_needed = {'nickname', 'role', 'created_at'}
        cookies_ds = yaml.unsafe_load(cookies_decoded)
        if bool(cookies_needed ^ cookies_ds.keys()):
            return jsonify({'error': 'Bad cookies'})

        return User(cookies_ds).get_data()
    except:
        traceback.print_exc()
        return jsonify({'error': 'Bad cookies decode'})