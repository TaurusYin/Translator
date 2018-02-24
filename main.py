from flask import Flask, jsonify
from functools import wraps
from flask import make_response
import Filehandler
import os

app = Flask(__name__)

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

@app.route('/todo/api/v1.0/translate/<path:path>', methods=['GET'])
@allow_cross_domain
def translate_path(path):
    print(path)
    if path == '' or not os.path.exists(path):
        return jsonify({'info': 'cannot find the path'+ path})
    else:
        result = Filehandler.translate_from_path(path)
        return jsonify({'info': result})
if __name__ == '__main__':
    app.run(debug=True)