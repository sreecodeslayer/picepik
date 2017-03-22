from flask import Flask,render_template, url_for, request, jsonify, redirect
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from flask_mongoengine import MongoEngine, DoesNotExist
from settings import db,app
from modals import User, AddressBook
import bcrypt
from uuid import uuid4

# now get all the models from models.py ( this can be inside app.py)
# am just making it in models.py for readbility

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user):
	return User.objects.get(id=user)

# ------------------------------------------------------------------------------------
#										 Flask Login ends
# ------------------------------------------------------------------------------------

@app.route('/')
def index():
	try:
		return render_template('index.html',page='index',username=current_user.username)
	except Exception as e:
		return render_template('index.html',page='index',username=None)


@app.route("/login", methods=['POST'])
def login():
	params = request.get_json()['creds']
	try:
		user = User.objects.get(username=params['username'])
		if user.validate_login(user.password, params['password']):
			user_obj = User.objects.get(id=user.id)
			login_user(user_obj)
			return jsonify({'status': True})
	except DoesNotExist:
		return jsonify({'status': False})
	return jsonify({'status': False})


@app.route("/signup", methods=['POST'])
def signup():
	print request.get_json()
	params = request.get_json()['creds']
	try:
		data = User.objects.get(username=params['username'])
		return jsonify({'status': False})
	except DoesNotExist:

		hashed_pass = bcrypt.hashpw(str(params['password']), bcrypt.gensalt())
		user_obj = User(username=params['username'])
		user_obj.set_password(params['password'])
		user_obj.save()
		return jsonify({'status':True})

@app.route("/logout", methods=['POST'])
def logout():
	try:
		logout_user()
		return jsonify({'status':True})
	except:
		return jsonify({'status':False})

@app.route('/contact')
def contact():
	try:
		return render_template('contact.html',page='contact',username=current_user.username)
	except Exception as e:
		return render_template('contact.html',page='contact',username=None)

@app.route('/portfolio')
def portfolio():
	try:
		return render_template('portfolio.html',page='portfolio',username=current_user.username)
	except Exception as e:
		return render_template('portfolio.html',page='portfolio',username=None)

@app.route('/portfolio/product', methods=['GET'])
def product_page():
	return render_template('product.html',page='product')

@app.route('/portfolio/orders', methods=['GET'])
def orders_page():
	return render_template('orders.html',page='orders')

@app.route('/portfolio/address-book', methods=['GET'])
def address_book_page():
	try:
		return render_template('address.html',page='address',username=current_user.username)
	except Exception as e:
		return render_template('address.html',page='address',username=None) 

@app.route('/portfolio/address-book/new', methods=['POST'])
def address_book_new():
	address = request.get_json()['address']

	print address
	return jsonify({'status':True})
if __name__ == "__main__":
	app.run()
