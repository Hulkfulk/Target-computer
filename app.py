from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def base():
    return render_template("home.html")

@app.route('/course')
def course():
    return render_template("courses.html") 

@app.route('/price')
def price():
    return render_template("price.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__=='__main__':
    app.run(debug=true)    