from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# User import secrets,
# secrets.token_hex(16) in Python command line
app.config['SECRET_KEY'] = 'e112fc8128eaec1d609dfc594f1fcb45'

posts = [
    {
        'author': 'Mosheh EliYahu',
        'title': 'Climbing Everest',
        'content': 'The challenges of climbing Mt Everest are "a headache material right there!"',
        'date_posted': '20 May, 2018'
    },
    {
        'author': 'Seiko EliYahu',
        'title': 'Visiting Japan',
        'content': 'Bullet train experience wat breath taking.',
        'date_posted': '10 Jan, 2019'
    },
    {
        'author': 'Tom Saleeba',
        'title': 'Cycling in Canada',
        'content': 'The scenic views in British Colombia were beyond belief.',
        'date_posted': '16 Feb, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
