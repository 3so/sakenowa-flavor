import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest

from sakenowa_flavor import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# アクセス時にページが表示される

def test_get_root(client):
    result = client.get('/')
    assert u'日本酒フレーバー検索' in result.data.decode()

### 絞り込み検索
## 地域選択時に該当する地域の酒蔵が表示される

def select_search(client, url, area_id, brewery_id=None, brand_id=None):
    return client.post(url, data=dict(
        area=area_id,
        brewery=brewery_id,
        brand=brand_id
    ))

def test_select_area(client):
    result = select_search(client, 'select_area', 1)
    assert u'高砂酒造' in result.data.decode()

## 酒蔵選択時に該当する地域の銘柄が表示される

def test_select_brewery(client):
    result = select_search(client, 'select_brewery', 1, 6)
    assert u'国士無双' in result.data.decode()

## 銘柄選択
# フレーバーチャート、フレーバータグがあれば表示する
# フレーバーチャート、フレーバータグがなければその旨表示する
def test_select_brand(client):
    result = select_search(client, 'select_brand', 1, 6, 10)
    assert u'plotly' in result.data.decode()
    assert u'フルーティ' in result.data.decode()

    result = select_search(client, 'select_brand', 1, 6, 3325)
    assert u'フレーバーチャートはありません' in result.data.decode()
    assert u'情報がありません' in result.data.decode()

### 銘柄名入力検索
def input_search(client, url, input_brand, selected_brand=None):
    return client.post(url, data=dict(
        input_brand=input_brand,
        selected_brand=selected_brand
    ))

## 入力した文字列を含む銘柄を検索・表示する
def test_search_brand(client):
    result = input_search(client, 'search_brand', '国')
    assert u'国士無双' in result.data.decode()

## 選択した銘柄の情報を表示する
# フレーバーチャート、フレーバータグがあれば表示する
# フレーバーチャート、フレーバータグがなければその旨表示する
def test_select_search_brand(client):
    result = input_search(client, 'select_search_brand', '国', 10)
    assert u'plotly' in result.data.decode()
    assert u'フルーティ' in result.data.decode()

    result = input_search(client, 'select_search_brand', '国', 962)
    assert u'フレーバーチャートはありません' in result.data.decode()
    assert u'情報がありません' in result.data.decode()

#app.config['TESTING'] = True
#client = app.test_client()
#result = input_search(client, 'search_brand', '国')
#print(result.data.decode())