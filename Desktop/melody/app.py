from flask import Flask, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
import os


# mysql = MySQL()
app = Flask(__name__)

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '000
# app.config['MYSQL_DATABASE_DB'] = 'music'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# mysql.init_app(app)

@app.route("/")
def index():
    return render_template("MelodyTest.html")
        


@app.route("/ResultPage", methods=['GET', 'POST'])
def result(file=None):
    if request.method == 'POST':
        temp = request.files['recorded']
        temp.save('./static/src/audio/' + secure_filename(temp.filename))
    elif request.method == 'GET':
        pass
    return render_template("ResultPage.html", file=temp)





if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8000)), debug=True, use_reloader=False)
