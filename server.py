from flask import Flask, jsonify, render_template, make_response, request
app = Flask(__name__)
import datetime
# localhost or ipだと何故かクッキー送信できないのでhostでフォワーディングする事
clinet_origin = 'http://localhost.test.com:1000'
# localhost or ipだと何故かクッキー送信できないのでhostでフォワーディングする事
server_domain = 'server.test.com'

## api
@app.route('/api/helloworld', methods=["GET"])
def api():
    response = make_response(jsonify({'message': 'Hello world', 'coockie': request.cookies}))
    # クレデンシャルが必要な場合は、オリジンに*はNG
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    # response.headers.add('Access-Control-Allow-Headers', "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept")
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    # SameSite
    #   None:Cookieを送信する
    #   Lax: 別ドメインからはPOST, ifram, XHR等のリクエストにクッキーがセットされない。
    #   Strict: 同一オリジンのリクエストのみクッキーを送信
    # domain
    #   このオプションをしていないと同一ドメインからのみ利用可能なクッキーになる
    #   ブラウザがクッキーを送信するサーバーのドメイン名
    #   ここで設定された値と送信先のサーバーのドメインがマッチするときだけクライアントからクッキーを送信する
    #   少なくともドットが2つ必要
    # サイドAから別ドメインのクッキーを書き込む = サードパーティークッキー
    response.set_cookie("get", value='2511',
                        httponly=True, samesite=None,
                        domain=server_domain, path='/')
    return response

@app.route("/api/post", methods=["POST"])
def post():
    response = make_response(jsonify({'message': 'post', 'coockie': request.cookies}))
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    response.headers.add('Origin', clinet_origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorizations,X-Requested-With, X-HTTP-Method-Override')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.set_cookie("post", value='2', httponly=True, samesite='Lax',
                        domain=server_domain, path='/')
    return response

@app.route("/api/put", methods=["PUT", "OPTIONS"])
def put():
    response = make_response(jsonify({'message': 'put'}))
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    response.headers.add('Access-Control-Allow-Headers', 'X-Custom-Header')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, OPTIONS')
    response.headers.add('Access-Control-Max-Age', 1)
    # 資格情報の送信に必要
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
