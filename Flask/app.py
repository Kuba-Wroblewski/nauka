from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc0ed4935868eeba22b8244b9eadfb57'

posts = [
    {
        'autor': 'Jakub Wróblewski',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 23, 2020'
    },
    {
        'autor': 'Jane Porn',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'April 24, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
