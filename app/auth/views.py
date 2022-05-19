from app.forms import LoginForm

from app import auth

@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }
    return ''