import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *

import core.feature_extract

now_url = '192.168.115.81'
UPLOAD_FOLDER = r'./uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app = Flask(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    typ = request.form.get('type')

    if typ == '':
        typ = 'E'
    print("前端选择的类型：", typ)

    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)

        image_path = os.path.join(r'./uploads', file.filename)

        result = core.feature_extract.Search_img(image_path, typ)

        # 返回需要显示的url
        return jsonify({'status': 1,
                        'image_url': f'http://{now_url}:5003/uploads/' + file.filename,
                        'draw_url1': f'http://{now_url}:5003/dataset/image_data/' + result[0],
                        'draw_url2': f'http://{now_url}:5003/dataset/image_data/' + result[1],
                        'draw_url3': f'http://{now_url}:5003/dataset/image_data/' + result[2],
                        'draw_url4': f'http://{now_url}:5003/dataset/image_data/' + result[3],
                        'draw_url5': f'http://{now_url}:5003/dataset/image_data/' + result[4],
                        'image_info': []})

    return jsonify({'status': 0})


@app.route('/upload2', methods=['GET', 'POST'])
def upload_file2():
    url = request.form.get('las')
    typ = request.form.get('type')

    image_path = os.path.join(r'./uploads', url)

    if typ == '':
        typ = 'E'
    print("前端选择的类型：", typ)

    result = core.feature_extract.Search_img(image_path, typ)

    # 返回需要显示的url
    return jsonify({'status': 1,
                    'image_url': f'http://{now_url}:5003/uploads/' + url,
                    'draw_url1': f'http://{now_url}:5003/dataset/image_data/' + result[0],
                    'draw_url2': f'http://{now_url}:5003/dataset/image_data/' + result[1],
                    'draw_url3': f'http://{now_url}:5003/dataset/image_data/' + result[2],
                    'draw_url4': f'http://{now_url}:5003/dataset/image_data/' + result[3],
                    'draw_url5': f'http://{now_url}:5003/dataset/image_data/' + result[4],
                        'image_info': []})


# 用不上
# @app.route("/download", methods=['GET'])
# def download_file():
#     # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
#     return send_from_directory('data', 'testfile.zip', as_attachment=True)


# show photo
@app.route('/uploads/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if file is not None:
            image_data = open(f'uploads/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


# show photo2
@app.route('/dataset/image_data/<path:file>', methods=['GET'])
def show_photo2(file):
    if request.method == 'GET':
        if file is not None:
            image_data = open(f'dataset/image_data/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    app.run(host=now_url, port=5003, debug=True)
    print("后端开始运行")
