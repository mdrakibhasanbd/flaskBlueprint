from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"hello world": "hello world"}


if __name__ == '__main__':
    app.run(debug=True, port=5008, host='0.0.0.0')
