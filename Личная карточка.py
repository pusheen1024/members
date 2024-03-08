import json
from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/member')
def member():
    members = json.load(open('templates/members.json', encoding='utf8'))
    return render_template('member.html', members=members)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')