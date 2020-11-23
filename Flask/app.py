from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
