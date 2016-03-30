# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10008)

