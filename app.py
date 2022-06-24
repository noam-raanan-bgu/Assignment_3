from flask import Flask ,redirect ,url_for
from  flask import render_template
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)