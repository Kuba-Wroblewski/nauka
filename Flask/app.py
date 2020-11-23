from flask import Flask, render_template, url_for
<<<<<<< HEAD
from 
# from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Task %r>' % self.id

=======

app = Flask(__name__)
>>>>>>> cc58aed5be856dfc27283c3471355ab71050972f

@app.route('/')
def index():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)