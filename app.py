from flask import jsonify


def do_calculation(data_from_server):
    return jsonify(data_from_server.values()[0])

