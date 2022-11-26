import os
from flask import (
    Flask, 
    session,
    request,
    render_template, 
    jsonify,
    make_response,
    )
from flask_login import (
    LoginManager, 
    login_required, fresh_login_required,
    current_user, login_user, logout_user, 
    )
from flask_cors import CORS


# https 를 쓰지 않을 경우, 보안 이슈로 에러가 남 (다음 설정을 통해 http 에서도 에러가 나지 않도록 함)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = Flask(__name__, static_url_path='/static')
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)
app.secret_key = 'pancho_server'