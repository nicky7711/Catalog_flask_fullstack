import json
from flask import make_response

from db.database_setup import Item


# populate item from request post
def item_from_request_post(request):
    if request.form['name']:
        item = Item()
        item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
            return item
    return None   # name and description required


# export to json
def json_response(msg, code):
    response = make_response(json.dumps(msg), code)
    response.headers['Content-Type'] = 'application/json'
    return response
