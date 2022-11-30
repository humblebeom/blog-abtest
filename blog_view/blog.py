from flask import (
    Flask, 
    Blueprint,
    request,
    render_template, make_response, jsonify,
    redirect, url_for,
    session
    )
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
from flask_login import login_user, logout_user, current_user
import datetime



blog_abtest = Blueprint('blog', __name__)
 

@blog_abtest.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == 'GET':
        print(request.headers)
        print(request.args.get('user_email'))
        # return make_response(jsonify(success=True), 200) 
        # return redirect(url_for('blog.test_blog'))
        return redirect(url_for('/blog.blog_fullstack1'))
    else:
        print(request.headers)
        # content type 이 application/json 인 경우 -> request.get_json()
        # content type 이 application/json 가 아닌 경우(application/x-www-form-urlencoded) -> request.form
        # print('set_email', request.form['user_email'])
        # print('set_email', request.form['blog_id'])
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
          
        return redirect(url_for('blog.blog_fullstack1'))
    
@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog_fullstack1'))
    
@blog_abtest.route('/blog_fullstack1')
def blog_fullstack1():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)
