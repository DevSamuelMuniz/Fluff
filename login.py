from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
   nome = StringField('Seu Nome', validators=[InputRequired()])
   email = StringField('Email', validators=[InputRequired()])
   senha = PasswordField('Senha', validators=[InputRequired()])
   confirmarSenha = PasswordField('Confirmar senha', validators=[InputRequired(), EqualTo('senha')])

@app.route('/login', methods=['GET', 'POST'])
def login():
 form = LoginForm()
 if form.validate_on_submit():
    name = form.nome.data
    email = form.email.data
    senha = form.senha.data

 return render_template('login.html', form=form)

