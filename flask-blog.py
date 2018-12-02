from flask import Flask, render_template
app = Flask(__name__)

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
    data = {"title": "Home", "posts": posts} 
    return render_template('home.html', param=data)


@app.route('/about')
def about():
    title = {"title": "About"}
    return render_template('about.html', param=title)


if __name__ == "__main__":
    app.run(debug=True)
