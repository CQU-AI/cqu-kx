from flask import Flask, render_template

from cqu_kx.__main__ import server_main

app = Flask(__name__)


@app.route('/<username>/<password>')
def get_ical(username, password):
    table = server_main(username, password)
    table = table.replace("<th>", "<th><h1>").replace("</th>", "</h1></th>").replace('border="1"', "")

    return render_template('template.html', username=username, table=table)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
