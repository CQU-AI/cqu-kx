import os

from flask import Flask, render_template, Markup, session

from cqu_kx.__main__ import server_main

app = Flask(__name__)
app.secret_key = b"\x00" + os.urandom(10) + b"\x00"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/go')
def go():
    if "username" not in session:
        return render_template('404.html'), 404
    table = server_main(session["username"], session["password"])
    table = table.replace("<th>", "<th><h1>").replace("</th>", "</h1></th>").replace('border="1"', "")
    session["result"] = table
    return "ok"


@app.route('/done')
def done():
    if "username" not in session:
        return render_template('404.html'), 404
    return render_template('table.html', username=session["username"], table=session["result"])


@app.route('/<username>/<password>')
def get_ical(username, password):
    session['username'] = username
    session['password'] = password
    return render_template("redirect.html")


@app.route('/refresh')
def refresh():
    if "username" not in session:
        return render_template('404.html'), 404
    return render_template("redirect.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
