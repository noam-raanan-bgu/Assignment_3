from flask import Blueprint, render_template, redirect, flash, request
from db_manager import interact_db

# Assignment_4 blueprint definition
Assignment_4 = Blueprint('Assignment_4', __name__, static_folder='static', static_url_path='/Assignment_4',
                         template_folder='templates')


@Assignment_4.route('/Assignment_4')
def Assignment_4_func():
    query = "select * from users;"
    users = interact_db(query=query, query_type='fetch')
    return render_template('Assignment_4.html', users=users)


@Assignment_4.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query2 = "select * from Users where EMAIL='%s';" % email
    numOfUsers = interact_db(query=query2, query_type="fetch")
    if len(numOfUsers) == 0:
        query = " INSERT INTO users(USER_NAME, EMAIL, PASSWORD) VALUES ('%s', '%s', '%s');" % (name, email, password)
        interact_db(query=query, query_type="commit")
        flash(message="You have added a new user successfully !")
    else:
        flash(message="This Email address is already in the system!")

    return redirect('/Assignment_4')


@Assignment_4.route('/delete_users', methods=['POST'])
def delete_users_func():
    email = request.form['email']
    query2 = "select USER_NAME from Users where EMAIL='%s';" % email
    numOfUsers = interact_db(query=query2, query_type="fetch")
    if len(numOfUsers) != 0:
        query = " DELETE FROM users WHERE EMAIL='%s';" % email
        interact_db(query=query, query_type="commit")
        flash(message="The user was deleted successfully from the DB!")
    else:
        flash(message="This Email address is not in the system!")

    return redirect('/Assignment_4')


@Assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    email = request.form['email']
    password = request.form['password']
    query2 = "select * from Users where EMAIL='%s';" % (email)
    numOfUsers = interact_db(query=query2, query_type="fetch")
    if len(numOfUsers) != 0:
        query = " UPDATE users SET PASSWORD='%s' WHERE EMAIL ='%s' ;" % (password, email)
        interact_db(query=query, query_type="commit")
        flash(message="You have successfully updated the user's password!")
    else:
        flash(message="This Email address is not in the system! please try again.")

    return redirect('/Assignment_4')


