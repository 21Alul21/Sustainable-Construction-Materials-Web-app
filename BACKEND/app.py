
from flask import Flask, render_template, url_for, redirect, request, flash
from models.databaseModel import db, Users, Posts, Comments, Reactions
from models.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')


db.init_app(app)
bcrypt = Bcrypt()
bcrypt.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """ function that loads the user into the session
    using their ID"""
    user = Users.query.get(int(user_id))
    return user

@app.route('/', strict_slashes=False)
def index():
   """ landing page view function"""
   return render_template('landing_page.html')


@app.route('/about_me', strict_slashes=False)
def about_me():
    """ about me view function"""
    title = 'about page'
    return render_template('about_me.html', title=title)


@app.route('/create_post', strict_slashes=False)
#@login_required
def create_post():
    """ view function that renders a template
    for creating post on the app
    """
    if current_user.is_authenticated:
        return render_template('create_post.html')
    else:
        return redirect(url_for('login'))


@app.route('/home', strict_slashes=False)
def home():
    """view function for the hompage
    where posts are created
    """
    title = 'home page'
    post = Posts.query.order_by(Posts.id.desc()).all()
    return render_template('home.html', title=title, post=post)


@app.route('/login_form', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ view function that handles the logic
    for the login form
    """

    form = LoginForm()
    if form.validate_on_submit():

        user = Users.query.filter_by(user_name=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data): 
                flash('login successful, welcome {}'.format(user.user_name))
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('home'))
    return render_template('login_form.html', form=form)


@app.route('/register', strict_slashes=False, methods=['GET', 'POST'])
def registration():
    """ view function that handles the registeration
    logic
    """

    form = RegistrationForm() 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = Users(user_name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))   
    return render_template('registration.html', form=form)


@app.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))
    

@app.route('/edit_post', methods=['GET', 'POST'])
def edit_post():
    return render_template('edit_post.html')






@app.route('/post', strict_slashes=False, methods=['POST'])
def post():
    
    if request.method == 'POST':
        post = request.form['post']
        new_post = Posts(post_field=post, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
    
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
