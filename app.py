from flask import Flask, redirect, url_for, request
from flask import render_template, session
app = Flask(__name__)
app.secret_key = '123'

#Part B

@app.route('/')
def cv_main_page():
    return render_template('CV.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/experience')
def experience_page():
    return render_template('experience.html')

@app.route('/assignment3_1')
def assignment3_page():
    return render_template('assignment3_1.html', name='Noam Raanan' ,sport2='football' , prog='sql' , prog2='JAVA', shows=('Friends' , 'Sienfeld' , 'Stranger Things' , 'The Office US' , 'The Pijamas' , '24'))

@app.route('/header')
def header_page():
    return render_template('header.html')

#Part C
users = {
    'NOAM': {'name': 'noam', 'email': 'noamraanan55@gmail.com'},
    'TAMAR': {'name': 'tamar', 'email': 'tamar7595@gmail.com'},
    'GIDEON': {'name': 'gideon', 'email': 'graanan@gmail.com'},
    'SARAH': {'name': 'sarah', 'email': 'sarahra@gmail.com'},
    'CHUBBY': {'name': 'chubby', 'email': 'chubbychub@gmail.com'}
}

@app.route('/assignment3_2', methods=['GET','POST'])
def search_3_2():


    if request.method == 'GET':
        if 'name' in request.args and 'email' in request.args and 'is_submit' in request.args:
            name = request.args['name']
            email = request.args['email']
            is_submit = request.args['is_submit']


            for value in users.values():
                if(value.get("name") == name and value.get("email") == email):
                    return render_template('assignment3_2.html', name=name, email=email)


            if(is_submit):
                return render_template('assignment3_2.html', users=users)
        return render_template('assignment3_2.html')


    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if 'username' in request.form:
            session['username'] = username
            return render_template('assignment3_2.html', username=username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('assignment3_2.html')

if __name__ == '__main__':
    app.run(debug=True)