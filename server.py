#!/usr/bin/env python

from flask import Flask, render_template
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


@app.route('/')
def display_counter():
    return render_template('index.html')


def main():

    app.run(port=8000)


if __name__ == '__main__':
    main()
