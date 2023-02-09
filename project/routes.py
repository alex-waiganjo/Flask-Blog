from . import app,db
from project.forms import LoginForm,RegistrationForm
from project.models import User
from flask_login import current_user,login_user,logout_user,login_required
from flask import render_template,flash,redirect,url_for,request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
   
    #Rendering some dummy data to the UI  
    
    users = [{
        'name':'alex',
        'gender':'male',
        'course':'IT',
        'location':'Muranga'
          },{
        'name':'ken',
        'gender':'male',
        'course':'Bcom',
        'location':'Nyandarua'
    },{
        'name':'jane',
        'gender':'female',
        'course':'Bcom',
        'location':'Nairobi'
    }]
    return render_template('index.html',users=users)
    # return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))        
        flash('Logged in Successfully!')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
