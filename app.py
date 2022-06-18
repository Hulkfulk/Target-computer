from flask import Flask,render_template, request
from flask_wtf import Form
from wtforms import StringField,PasswordField,IntegerField,SubmitField,EmailField,validators
app=Flask(__name__)


class SignupForm(Form):
    name=StringField("Name",[validators.DataRequired("Enter Your name"),validators.length(min=3)])
    phone=IntegerField("Phone Number",[validators.DataRequired("Enter the Phone number"),validators.length(min=10,max=12)])
    email=EmailField("Email",[validators.DataRequired("enter Your E-mail"),validators.length(min=5,max=90)])
    submit=SubmitField("Submit")

@app.route('/signup')
def signup():
    form=SignupForm()
    return render_template("signup.html",form=form)    

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
    app.run(debug=True)    