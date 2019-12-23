from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "09cd7581b41fc9bec9a9df0c38974371"

data = [
    {
        'author': 'Vishal Varghese',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 06, 2019',
     },
{
        'author': 'Ben Philip',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 01, 2019',
     },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
