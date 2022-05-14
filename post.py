from flask import Flask, render_template

app = Flask(__name__)

post = [
    {
        'author': 'Elvis',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    },
    {
        'author': 'Lornah',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    },
    {
        'author': 'Hope',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    }
]


@app.route("/")
def hello_world():
    return render_template('index.html', posts=post)


@app.route("/profile")
def profile():
    return render_template('profile.html', title='User Profile')



if __name__ == "__main__":
    app.run(debug=True)

