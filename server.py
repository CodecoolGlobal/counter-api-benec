#!/usr/bin/env python

from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

counter = 0

@app.route('/counter', methods=['GET'])
def get_counter():
    '''Return the actual value of the counter'''
    return jsonify({'value': counter})


def main():

    app.run(port=5000)


if __name__ == '__main__':
    main()
