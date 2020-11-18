
app = Flask(__name__)
Articles = Articles()

@app.route('/')
def index():
   return render_template('shop.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/articles')
def articles():
   return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
   return render_template('article.html', id=id)

class RegisterForm(Form):
   name = StringField('Name', [validators.Length(min=1, max=50)])
   username = StringField('Username', [valdiators.Length(min=4, max=25)])
   email = StringField('Email', [valdiators.Length(min=6, max=50)])
   password = PasswordFiels('Password', [
      valdiators.DataRequired(),
      validators.EqualTo('confirm', message='Passwords do not match')
   ])
   confirm = PasswordFiels('Confirm Password')

@app.route("/register",methods=['GET', 'POST'])
def register():
   form = RegisterForm(request.form)
   if request.method == 'POST' and form.validate():
         return render_template('register.html')
   return render_template('register.html', form=form)


if __name__== "__main__":
    app.run(debug=True)


   


