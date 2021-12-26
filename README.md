# corsのお勉強

## corsとは
異なるオリジン間のhttp通信でリソース(webサーバー)へのアクセス権を制御する仕組み<br>
オリジン = 通信プロトコル + ドメイン + ポート番号<br>

## 環境構築
クロスオリジン間でクッキーを送信する場合はlocalhost又はipだと何故か送信されない。<br>
ローカルで実行する際はhosts等でフォワーディングする事<br>
#### C:\Windows\System32\drivers\etc\hosts
```
127.0.0.1 localhost.test.com
172.20.193.203 server.test.com　※172.20.193.203 == プライベートipアドレス
```

#### フロント起動
```
$ python3 client.py
```

#### バックエンド起動
```
$ python3 server.py
```

## 思ったこと
localでクロスオリジン環境の設定がめんどくさい。<br>
ローカルだとなんかよくわからんけど動かんみたいな事があってステージング環境がほしい！ってなった。<br>
フロント、バックエンドを切り離すと意識する事が多そうで大変<br>
spa用のapiならsamesite=Noneでよさそう。Laxだとpost時にクッキー内のtokenが使えないから<br>
リダイレクトレスポンスでリクエスト元を指定するとcorsで怒られるのが謎。<br>
<img src="https://user-images.githubusercontent.com/72111956/147396385-7cf0185c-1b59-4173-8f5f-07a7c214e89b.png">



# 参考サイト
https://qiita.com/att55/items/2154a8aad8bf1409db2b<br>
https://www.tohoho-web.com/ex/same-origin-policy.html<br>
https://ja.javascript.info/fetch-crossorigin<br>
https://dev.to/lydiahallie/cs-visualized-cors-5b8h<br>
