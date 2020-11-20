import os, pyodbc
import configparser
from flask import Flask, send_file, Response, send_from_directory, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder='static/')
CORS(app, resources={r'/*': {'origins': '*'}})
config = configparser.ConfigParser()
config.read('settings.ini')
db = pyodbc.connect(
    driver="{SQL Server Native Client 11.0}",
    server=config['DEFAULT']['Server'],
    database=config['DEFAULT']['Database'],
    user=config['DEFAULT']['User'],
    password=config['DEFAULT']['Password'],
    trusted_connect="no",
    Encrypt="yes"
)


@app.route('/')
def index_client():
    entry = os.path.join('..', 'Frontend', 'dist', 'index.html')
    return send_file(entry)


@app.route('/js/<path:filename>')
def static_js(filename):
    return send_from_directory(os.path.join('..', 'Frontend', 'dist', 'js'), filename)


@app.route('/css/<path:filename>')
def static_css(filename):
    return send_from_directory(os.path.join('..', 'Frontend', 'dist', 'css'), filename)


@app.route('/api/unit', methods=['GET'])
def units_get():
    cursor = db.cursor()
    cursor.execute('SELECT DISTINCT device_id FROM device_measurements ORDER BY device_id ASC')
    data = []
    for row in cursor:
        data.append(dict(zip([column[0] for column in cursor.description], row)))

    if len(data) > 0:
        return jsonify(data)

    return Response('', status=404)


@app.route('/api/unit/<unit>', methods=['GET'])
def unit_get(unit):
    cursor = db.cursor()
    cursor.execute('SELECT TOP 1 * FROM device_measurements WHERE device_id=? ORDER BY sent_timestamp DESC', unit)
    for row in cursor:
        return dict(zip([column[0] for column in cursor.description], row))

    return Response('', status=404)


@app.route('/api/unit/<unit>/history', methods=['GET'])
def unit_history_get(unit):
    try:
        rows = int(request.args.get('rows'))
    except ValueError:
        return Response('Rows requested is NaN', status=400)

    if rows < 1:
        return Response('Too few rows requested (< 1)', status=400)

    if rows > 1000:
        return Response('Too many rows requested (> 1000)', status=400)

    cursor = db.cursor()
    cursor.execute('SELECT TOP {} * FROM device_measurements WHERE device_id=? ORDER BY sent_timestamp DESC'.format(rows), unit)
    data = []
    for row in cursor:
        data.append(dict(zip([column[0] for column in cursor.description], row)))

    if len(data) > 0:
        return jsonify(data)

    return Response('', status=404)


# app.run(port=5001)
