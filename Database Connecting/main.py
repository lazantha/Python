from flask import Flask,render_template,url_for,request,redirect,flash
from form import AdminSignUp
from connect import TableCreation
# from connect import TableCreation
app=Flask(__name__)
app.config['SECRET_KEY']="kEY"
# bcrypt=Bcrypt(app)

@app.route('/' ,methods=['GET','POST'])
def index():
	name=None
	new_form=AdminSignUp()	
	if new_form.validate_on_submit():
		first_name=new_form.first_name.data
		last_name=new_form.last_name.data
		email=new_form.email.data
		flash(f'Account has been created ! {form.first_name.data}')
		return redirect(url_for('/'))

	return render_template('index.html',form=new_form,name=first_name)