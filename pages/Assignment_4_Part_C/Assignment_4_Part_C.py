from flask import Blueprint, jsonify
from db_manager import interact_db


Assignment_4_Part_C = Blueprint('Assignment_4_Part_C', __name__, static_folder='static',
                                static_url_path='/Assignment_4_Part_C/static',
                                template_folder='templates')


@Assignment_4_Part_C.route('/Assignment_4/restapi_users', defaults={'user_id': 1})
@Assignment_4_Part_C.route('/Assignment_4/restapi_users/<int:user_id>')
def Assignment_4_Part_C_user_func(user_id):
    query = 'select  USER_ID,USER_NAME,EMAIL from users where USER_ID=%s;' % user_id
    users = interact_db(query=query,query_type="fetch")
    if len(users) == 0 :
        user_dict = {
            'status' : 'failed' ,
            'message' : 'user not found'
        }
    else:
        user_dict = {
            'status': 'success',
            'id': users[0].USER_ID,
            'name': users[0].USER_NAME,
            'email': users[0].EMAIL
        }
    return jsonify(user_dict)
