
from flask import Flask, make_response, render_template, url_for, redirect, request
from models.databaseModel import db, Users, Posts, Comments, Reactions
from models.forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'IUFGUI9FEVIDEGVIUDEGVDEVDIUUBVDSISB1121133000))'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db.init_app(app)


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
def create_post():
    """ view function that renders a template
    for creating post on the app
    """
    
    return render_template('create_post.html')


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
        return redirect(url_for('home'))
    return render_template('login_form.html', form=form)


@app.route('/register', strict_slashes=False, methods=['GET', 'POST'])
def registration():
    """ view function that handles the registeration
    logic
    """

    form = RegistrationForm() 
    if form.validate_on_submit():
        return redirect(url_for('login'))   
    return render_template('registration.html', form=form)


@app.route('/post', strict_slashes=False, methods=['POST'])
def post():
    
    post = request.form['post']
    new_post = Posts(post_field=post, user_id=2)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
