from flask import Blueprint,render_template,request,redirect,url_for
from database import *
public=Blueprint('public',__name__)


@public.route('/')
def index():
	return render_template("index.html")
@public.route('/login',methods=['get','post'])
def login():
	if 'submit'in request.form:
		uname=request.form['uname']
		pword=request.form['pword']

		q="SELECT * FROM `login`WHERE `username`='%s' AND `password`='%s'"%(uname,pword)
		res=select(q)
		if res:
			if res[0]['usertype']=="admin":
				return redirect(url_for("admin.admin_home"))
	return render_template("login.html")

@public.route('/register',methods=['get','post'])
def registration():
	if 'reg' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		phone=request.form['phone']
		gender=request.form['Gender']
		uname=request.form['uname']
		passw=request.form['pword']

		q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES('%s','%s','user')"%(uname,passw)
		ids=insert(q)
		q="INSERT INTO `registration`(`firstname`,`lastname`,`phone`,`gender`,`email`,`login_id`) VALUES('%s','%s','%s','%s','%s','%s')"%(fname,lname,phone,gender,email,ids)
		insert(q)

	return render_template("registration.html")
