from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import apiget
import json

app = Flask(__name__)

# メインページのルーティング
@app.route('/')
def index():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    areas = apiget.get_area()
    breweries = apiget.get_breweries(area_id)
    brands = apiget.get_brands(brewery_id)
    return render_template('index.html',
                            areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id)

# 絞り込み検索

# 地域の選択
@app.route('/select_area', methods=['GET', 'POST'])
def select_area():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    if request.form['area'].isdecimal():
        area_id = int(request.form['area'])
    areas = apiget.get_area()
    breweries = apiget.get_breweries(area_id)
    brands = apiget.get_brands(brewery_id)
    return render_template('index.html',
                            areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id)

# 蔵元の選択
@app.route('/select_brewery', methods=['GET', 'POST'])
def select_brewery():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    if request.form['area'].isdecimal():
        area_id = int(request.form['area'])
    if request.form['brewery'].isdecimal():
        brewery_id = int(request.form['brewery'])
    areas = apiget.get_area()
    breweries = apiget.get_breweries(area_id)
    brands = apiget.get_brands(brewery_id)
    return render_template('index.html',
                            areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id)

# 銘柄の選択
@app.route('/select_brand', methods=['GET', 'POST'])
def select_brand():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    if request.form['area'].isdecimal():
        area_id = int(request.form['area'])
    if request.form['brewery'].isdecimal():
        brewery_id = int(request.form['brewery'])
    if request.form['brand'].isdecimal():
        brand_id = int(request.form['brand'])
    areas = apiget.get_area()
    breweries = apiget.get_breweries(area_id)
    brands = apiget.get_brands(brewery_id)
    return render_template('index.html',
                            areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id)

# 絞り込み検索終わり

# 銘柄名検索



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')