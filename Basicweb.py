from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About', text='This is an about page')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")