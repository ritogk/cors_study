from flask import Flask, jsonify, render_template, make_response, request
app = Flask(__name__)

## 画面
@app.route('/')
def hello():
    return render_template('hello.html')

## おまじない
if __name__ == "__main__":
    app.run(host='localhost', port=1000, debug=True)
