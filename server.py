#!/usr/bin/env python

from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

counter = 0

@app.route('/counter', methods=['GET'])
def get_counter():
    '''Return the actual value of the counter'''
    return jsonify({'value': counter})


@app.route('/counter/increment', methods=['POST'])
def increment_counter():
    '''Increment the counter by one.'''
    global counter
    counter += 1

    return jsonify({'success': True})


def main():

    app.run(port=5000)


if __name__ == '__main__':
    main()
