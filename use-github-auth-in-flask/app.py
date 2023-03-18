from flask import Flask, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = '812848ea396c6aa794e6b6c9'

github = OAuth(app).register(
    name='github',
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@app.route('/')
def index():
    user = session.get('user_email')
    if user is None:
        login_url = url_for('login', _external=True)
        return f'<p><a href="{login_url}">Login</a></p>'
    logout_url = url_for('logout', _external=True)
    return f'<p>Welcome {user}! | <a href="{logout_url}">Logout</a></p>'


@app.route('/login')
def login():
    callback_uri = url_for('callback', _external=True)
    return github.authorize_redirect(callback_uri)


@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    resp = github.get('user', token=token)
    profile = resp.json()
    session['user_email'] = profile['email']
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect('/')


if '__main__' == __name__:
    app.run(debug=True)
