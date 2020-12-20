# アプリケーション名
日本酒フレーバー検索

# アプリケーション概要
[さけのわデータ](https://muro.sakenowa.com/sakenowa-data/)を利用することで、日本酒のフレーバーの傾向を
- 華やかさ・芳醇さなど6つの項目で評価したレーダーチャート
- 辛口・甘口など具体的な言葉でフレーバーを表現したフレーバータグ

の2点から確認することができる。

# URL
https://sake-flavor-app.herokuapp.com/

# 利用方法
「絞り込み検索」「銘柄名入力検索」の2種類の検索方法で日本酒の銘柄を検索できる。
## 絞り込み検索
***
「地域→蔵元→銘柄」という順に情報を絞り込んで検索できる。
1. 「地域」プルダウンリストから情報を知りたい地域を選択する。
1. 「蔵元」プルダウンリストから情報を知りたい蔵元を選択する。
1. 「銘柄」プルダウンリストから情報を知りたい銘柄を選択する。
1. 選んだ銘柄に紐づくフレーバー情報が表示される。

## 銘柄名入力検索
***
銘柄名の一部を入力することで、銘柄名を検索できる。
1. 「銘柄名入力検索」の下にあるテキストフォームに調べたい銘柄名を入力し「検索する」を押す。
1. 下のプルダウンメニューに表示された検索結果一覧から、情報を知りたい銘柄を選択する。
1. 選んだ銘柄に紐づくフレーバー情報が表示される。

また、検索情報を初期化したい場合は「初期化」ボタンを押すことで初期化できる。

# 目指した課題解決
日本酒のラベルや飲食店のメニューに書いてある情報は多くの場合アルコール度数、日本酒度、酸度、酒米の品種などとなっている。
これらと一般的な飲食物の味の評価（甘い、苦いなど）と結びつけることは難しく、特にあまり日本酒を飲んだことがない人はその情報のみから事前にその味や香りを予想することは困難である。
そのため、日本酒に興味があっても酒屋や飲食店で買うことはややハードルが高いと考えられる。
そこで、「日本酒に興味はあるがそこまでは詳しくない」という人が、自ら日本酒を飲む/買うことを考えたときに、日本酒の味・香りといったフレーバーを事前にわかりやすくするために本アプリを作成した。


# 洗い出した要件

## 銘柄名の入力による検索機能（銘柄名入力検索）
***
#### 目的
- 銘柄の名前を入力することで、目的の銘柄の情報を表示できるようにする
#### 詳細
- 銘柄名の一部を送信することで候補となる銘柄の一覧を返し、銘柄名で絞り込んで検索できるようにする
#### ストーリー
- 銘柄名の一部を送信したとき、候補となる銘柄名の一覧を返す
- 銘柄名の一覧から銘柄を選択すると、フレーバーの情報が表示される
- 該当する銘柄がない場合、「該当する銘柄は見つかりませんでした」と返す

## フレーバーチャートの表示
***
### 目的
- 味の傾向を見た目でわかりやすくする

### 詳細
- 銘柄に紐づくフレーバーの数値情報（6種）を視覚的にわかりやすくするため、それらの情報をレーダーチャートに落とし込み、画像として表示する

### ストーリー
- 情報を知りたい銘柄名を送信したとき、フレーバーの情報をレーダーチャートの形で返却する
- フレーバーの情報がない場合、「フレーバーの情報はありません」と返却する

## フレーバータグの表示
***
### 目的
- 味の傾向をわかりやすく理解できるようにする
### 詳細
- 銘柄に紐づくフレーバータグを表示する
### ストーリー
- 情報を知りたい銘柄名を検索したとき、銘柄に紐づくフレーバータグが表示される
- フレーバータグの情報がない場合「情報はありません」と表示する

## 地域からの銘柄名しぼりこみ検索機能（しぼりこみ検索）
***
### 目的
- 銘柄名だけでなく、地域や酒蔵の名前からも銘柄を絞り込みできるようにする
### 詳細
- 地域名を入力すると蔵元名を返却し、蔵元名を入力することで銘柄名を返却できるようにする
### ストーリー
- 地域名を選択すると蔵元一覧を表示する
- 蔵元を選択すると銘柄一覧を表示する
- 銘柄一覧から銘柄を選択すると、フレーバーの情報が表示される


# 実装した機能について
## しぼりこみ検索
***
地域、蔵元から銘柄名を絞り込むことで、選択した銘柄のフレーバー情報を表示させる。
フレーバー情報がない場合は「情報がありません」と表示する。
[動作例GIF](https://gyazo.com/0d4cab4e1b8c1896e05385a9eacb8870)

## 銘柄名入力検索
***
銘柄名の一部を入力することで、候補となる銘柄名の一覧を表示する。
情報を確認したい銘柄を選択することで、選択した銘柄のフレーバー情報を表示させる。
フレーバー情報がない場合は「情報がありません」と表示する。
[動作例GIF](https://gyazo.com/5a1e28954b54f2dc112ba60ffef2f3e4)


# 実装予定の機能

## 類似フレーバーの銘柄表示
### 目的
- 過去に飲んだことのある銘柄から、似た味の銘柄を探せるようにする
### 詳細
- 銘柄名のフレーバー情報を返却する際、その銘柄のフレーバー情報の下に「類似したフレーバーの銘柄」として銘柄名を表示する
### ストーリー
- 銘柄名入力検索、絞り込み検索どちらの場合でもフレーバー情報の返却時に類似したフレーバーの銘柄を0〜5種類表示する


# ローカルでの動作方法
 `git clone` 後、 ` python sakenowa_flavor.py` で実行可能。

    git clone https://github.com/3so/sakenowa-flavor.git
    cd sakenowa-flavor
    python sakenowa_flavor.py

また、アプリケーションサーバーとしてgunicornも利用可能。

    gunicorn sakenowa_flavor:app

## 動作環境
***
Pythonのバージョンは以下の通り。
- Python 3.9.0

必要な外部ライブラリは以下の通り。
- flask
- requests
- numpy
- pandas
- plotly
- gunicorn

導入していないライブラリがあれば、pipを用いて適宜インストールが必要。

    pip install flask
    pip install requests
    pip install numpy
    pip install pandas
    pip install plotly
    pip install gunicorn