from app import app,db,auth,storage
from flask import render_template, request, redirect, url_for
from flask import session as fsession
import calendar
import time

session = {
	'logged' : False,
	'user' : False,
	'username' : False,
	'visit' : False
}


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',logged = session['logged'], title='Home', user={'username' : 'Tanay'})

@app.route('/register')
def register():
	return render_template('register.html',title='Sign Up' ,logged = session['logged'], error = False)

@app.route('/login')
def login():
	return render_template('login.html', title='Log In',  logged = session['logged'])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
@app.route('/add_user', methods=['POST'])
def add_user():
	users = db.child("users").get()
	if True:
		for user in users.each():
			if user.val()['email'] == request.form.get('email'):
				return render_template('register.html',logged = session['logged'], error= True)
	timestamp = calendar.timegm(time.gmtime());
	db.child('users').child(timestamp).set({
		'username' : request.form.get('username'),
		'email' : request.form.get('email'),
		'password' : request.form.get('password'),
		'timestamp' : timestamp
	})
	fsession['user'] = timestamp
	session['logged'] = True
	fsession['username'] = request.form.get('username')

	data = {

		'data' : {
			'name' : fsession['username'],
			'bio' : '',
			'link' : 'websitename/profile/'+str(fsession['user'])
		}, 


		'links' : 		
			{
				'instagram' : {
					'link' : '',
					'status' : ''
				},
				'snapchat' : {
					'link' : '',
					'status' : ''
				},
				'twitter' : {
					'link' : '',
					'status' : ''
				},
				'whatsapp' : {
					'link' :'',
					'status' : ''
				},
				'facebook' : {
					'link' : '',
					'status' : ''
				},
				'linkedin' : {
					'link' : '',
					'status' : ''
				},
				'phone' : {
					'link' : '',
					'status' : ''
				},
				'email' : {
					'link' : '',
					'status' : ''
				},
				'youtube' : {
					'link' : '',
					'status' : ''
				},
				'tiktok' : {
					'link' : '',
					'status' : ''
				},
				'soundcloud' : {
					'link' : '',
					'status' : ''
				},
				'spotify' : {
					'link' : '',
					'status' : ''
				},
				'apple' : {
					'link' : '',
					'status' : ''
				},
				'venmo' : {
					'link' : '',
					'status' : ''
				},
				'cashapp' : {
					'link' : '',
					'status' : ''
				},
				'paypal' : {
					'link' : '',
					'status' : ''
				},
				'twitch' : {
					'link' : '',
					'status' : ''
				},
				'link' : {
					'link' : '',
					'status' : ''
				},
				'website' : {
					'link' : '',
					'status' : ''
				},
				'address' : {
					'link' : '',
					'status' : ''
				}
			}

	}

	db.child('user_data').child(timestamp).set(data)

	return redirect(url_for('setup_profile'))


@app.route('/setup_profile')
def setup_profile():
	if fsession['user'] == False or session['logged'] == False:
		return redirect(url_for('index'))
	return render_template('setup-profile.html', logged = session['logged'] , username = fsession['username'])




@app.route('/setup_db', methods=['POST'])
def setup_db():
	
	if fsession['user'] == False or session['logged'] == False:
		return redirect(url_for('index'))

	data = {

		'data' : {
			'name' : request.form.get('username'),
			'bio' : request.form.get('bio'),
			'link' : 'websitename/profile/'+str(fsession['user'])
		}, 


		'links' : 		
			{
				'instagram' : {
					'link' : request.form.get('instagram'),
					'status' : request.form.get('instagram_check')
				},
				'snapchat' : {
					'link' : request.form.get('snapchat'),
					'status' : request.form.get('snapchat_check')
				},
				'twitter' : {
					'link' : request.form.get('twitter'),
					'status' : request.form.get('twitter_check')
				},
				'whatsapp' : {
					'link' : request.form.get('whatsapp'),
					'status' : request.form.get('whatsapp_check')
				},
				'facebook' : {
					'link' : request.form.get('facebook'),
					'status' : request.form.get('facebook_check')
				},
				'linkedin' : {
					'link' : request.form.get('linkedin'),
					'status' : request.form.get('linkedin_check')
				},
				'phone' : {
					'link' : request.form.get('phone'),
					'status' : request.form.get('phone_check')
				},
				'email' : {
					'link' : request.form.get('email'),
					'status' : request.form.get('email_check')
				},
				'youtube' : {
					'link' : request.form.get('youtube'),
					'status' : request.form.get('youtube_check')
				},
				'tiktok' : {
					'link' : request.form.get('tiktok'),
					'status' : request.form.get('tiktok_check')
				},
				'soundcloud' : {
					'link' : request.form.get('soundcloud'),
					'status' : request.form.get('soundcloud_check')
				},
				'spotify' : {
					'link' : request.form.get('spotify'),
					'status' : request.form.get('spotify_check')
				},
				'apple' : {
					'link' : request.form.get('apple'),
					'status' : request.form.get('apple_check')
				},
				'venmo' : {
					'link' : request.form.get('venmo'),
					'status' : request.form.get('venmo_check')
				},
				'cashapp' : {
					'link' : request.form.get('cashapp'),
					'status' : request.form.get('cashapp_check')
				},
				'paypal' : {
					'link' : request.form.get('paypal'),
					'status' : request.form.get('paypal_check')
				},
				'twitch' : {
					'link' : request.form.get('twitch'),
					'status' : request.form.get('twitch_check')
				},
				'link' : {
					'link' : request.form.get('link'),
					'status' : request.form.get('link_check')
				},
				'website' : {
					'link' : request.form.get('website'),
					'status' : request.form.get('website_check')
				},
				'address' : {
					'link' : request.form.get('address'),
					'status' : request.form.get('address_check')
				}
			}

	}

	for d in data['links']:
		if data['links'][d]['status'] == False or data['links'][d]['status'] == None or data['links'][d]['status'] == 'null' :
			data['links'][d]['status'] = 'off'

	db.child('user_data').child(session['user']).update(data)

	return redirect('/profile')




@app.route('/user_login', methods=['POST'])
def user_login():
	users = db.child("users").get()
	for user in users.each():
		if user.val()['email'] == request.form.get('email'):
			if user.val()['password'] == request.form.get('password'):
				fsession['user'] = user.val()['timestamp']
				session['logged'] = True
				return redirect('/profile')
	return render_template('login.html',logged = session['logged'], error= True)


@app.route('/profile')
def profile():
	if fsession['user'] == False or session['logged'] == False:
		return redirect(url_for('index'))
	userdata = db.child('user_data').child(str(fsession['user'])).get()
	return render_template('profile.html', title = str(fsession['username']), logged = session['logged'], data = userdata.val() )


@app.route('/logout')
def logout():
	fsession['user'] = False
	session['logged'] = False
	fsession['username'] = False
	return redirect('/index')

@app.route('/edit_profile')
def edit_profile():
	if fsession['user'] == False or session['logged'] == False:
		return redirect(url_for('index'))
	userdata = db.child('user_data').child(str(fsession['user'])).get()
	return render_template('edit-profile.html', logged = session['logged'], title = 'Edit your profile', data = userdata.val())

@app.route('/update_db', methods = ['POST'])
def update_db():

	if fsession['user'] == False or session['logged'] == False:
		return redirect(url_for('index'))

	data = {

		'data' : {
			'name' : request.form.get('username'),
			'bio' : request.form.get('bio'),
			'link' : 'websitename/profile/'+str(fsession['user'])
		}, 


		'links' : 		
			{
				'instagram' : {
					'link' : request.form.get('instagram'),
					'status' : request.form.get('instagram_check')
				},
				'snapchat' : {
					'link' : request.form.get('snapchat'),
					'status' : request.form.get('snapchat_check')
				},
				'twitter' : {
					'link' : request.form.get('twitter'),
					'status' : request.form.get('twitter_check')
				},
				'whatsapp' : {
					'link' : request.form.get('whatsapp'),
					'status' : request.form.get('whatsapp_check')
				},
				'facebook' : {
					'link' : request.form.get('facebook'),
					'status' : request.form.get('facebook_check')
				},
				'linkedin' : {
					'link' : request.form.get('linkedin'),
					'status' : request.form.get('linkedin_check')
				},
				'phone' : {
					'link' : request.form.get('phone'),
					'status' : request.form.get('phone_check')
				},
				'email' : {
					'link' : request.form.get('email'),
					'status' : request.form.get('email_check')
				},
				'youtube' : {
					'link' : request.form.get('youtube'),
					'status' : request.form.get('youtube_check')
				},
				'tiktok' : {
					'link' : request.form.get('tiktok'),
					'status' : request.form.get('tiktok_check')
				},
				'soundcloud' : {
					'link' : request.form.get('soundcloud'),
					'status' : request.form.get('soundcloud_check')
				},
				'spotify' : {
					'link' : request.form.get('spotify'),
					'status' : request.form.get('spotify_check')
				},
				'apple' : {
					'link' : request.form.get('apple'),
					'status' : request.form.get('apple_check')
				},
				'venmo' : {
					'link' : request.form.get('venmo'),
					'status' : request.form.get('venmo_check')
				},
				'cashapp' : {
					'link' : request.form.get('cashapp'),
					'status' : request.form.get('cashapp_check')
				},
				'paypal' : {
					'link' : request.form.get('paypal'),
					'status' : request.form.get('paypal_check')
				},
				'twitch' : {
					'link' : request.form.get('twitch'),
					'status' : request.form.get('twitch_check')
				},
				'link' : {
					'link' : request.form.get('link'),
					'status' : request.form.get('link_check')
				},
				'website' : {
					'link' : request.form.get('website'),
					'status' : request.form.get('website_check')
				},
				'address' : {
					'link' : request.form.get('address'),
					'status' : request.form.get('address_check')
				}
			}

	}

	for d in data['links']:
		if data['links'][d]['status'] == False or data['links'][d]['status'] == None or data['links'][d]['status'] == 'null' :
			data['links'][d]['status'] = 'off'

	db.child('user_data').child(fsession['user']).update(data)

	return redirect('/profile')

@app.route('/visit/<user>')
def visit(user):
	fsession['visit'] = user
	return redirect('/user')

@app.route('/user')
def user():
	userdata = db.child('user_data').child(str(fsession['visit'])).get()
	return render_template('visit-profile.html', logged= session['logged'], title='visit profile', data = userdata.val())