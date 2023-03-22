from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route('/', methods = ["GET","POST"])
def base():       
      
    return render_template('index.html')


@app.route('/home', methods = ["GET","POST"])
def home():
       
      
    return render_template('index.html')


@app.route('/signup', methods=["GET","POST"])
def signup():

    form = SignUpForm()

    if form.validate_on_submit():
        #print out form info in terminal and redirect to home page
        first_name = form.first_name.data 
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(f'first: {first_name} last: {last_name} phone: {phone} address {address}')
        flash(f"Sign up was a Success!")
        return redirect(url_for('home'))
    
    return render_template('signup.html', form = form)
