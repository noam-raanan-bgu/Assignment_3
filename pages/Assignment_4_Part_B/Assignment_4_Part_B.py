from flask import Blueprint, render_template, redirect, flash, request,jsonify
from db_manager import interact_db
import collections
import json
import requests

# Assignment_4 blueprint definition
Assignment_4_Part_B = Blueprint('Assignment_4_Part_B', __name__, static_folder='static',
                                static_url_path='/Assignment_4_Part_B/static',
                                template_folder='templates')


@Assignment_4_Part_B.route('/Assignment_4/users')
def users_func():
    query = "Select * from Users;"
    users_list = []
    for row in interact_db(query, "fetch"):
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['name'] = row[1]
        d['email'] = row[2]
        d['password'] = row[3]
        users_list.append(d)
    users = json.dumps(users_list, default=str)
    return render_template('Assignment_4_Part_B.html', users=users)


@Assignment_4_Part_B.route('/Assignment_4/outer_source')
def outerUsers_func():
    if "id" in request.args:
        id = int(request.args['id'])
    user = requests.get(f'https://reqres.in/api/users/{id}',verify = False)
    user = user.json()
    print(user)
    return render_template('/Assignment_4_Part_B.html', user=user)
