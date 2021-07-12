from flask import Flask, render_template

app=Flask(__name__) # this gets the name of the file as the app name

@app.route("/") # this tells flask what URL to serve up
def hello_world():
    return "<p> Hello SEOTech developer </p>"

# # Let’s add an About page to our simple website.
# # First, pick the URL you want the page to be at – for example, website.com/about is pretty standard:
@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page')

@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page')


# put this code to bypass manual environent variable setting and server start
if __name__=='__main__': 
    app.run(debug=True, host="0.0.0.0")