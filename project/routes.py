from project import app
from project.forms import LoginForm
from flask import render_template,flash,redirect,url_for



@app.route('/index')
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

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #  flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
         flash('Login Successful')
         return redirect(url_for('index'))
    return render_template('login.html',form=form)
