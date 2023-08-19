from flask import flask ,request , jsonify

app = flask(__name__)

@app.route('/hello')

def hello():
        return"Hello,How are you"

if __name__="__main__":
    print("starting python flask server for a gocery store management system")

app.run(port=5000)

