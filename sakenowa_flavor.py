from flask import Flask, render_template, request, redirect, url_for
import apiget
import flavor_chart as fc

app = Flask(__name__)

# メインページのルーティング
@app.route('/')
def index():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    input_brand = ""
    search_brands = apiget.search_brands(input_brand)
    areas = apiget.get_area()
    breweries = apiget.get_breweries(area_id)
    brands = apiget.get_brands(brewery_id)
    return render_template('index.html',
                            areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)

# 絞り込み検索

# 地域の選択
@app.route('/select_area', methods=['GET', 'POST'])
def select_area():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    input_brand = ""
    search_brands = apiget.search_brands(input_brand)
    if request.method == 'POST':
        if request.form['area'].isdecimal():
            area_id = int(request.form['area'])
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)
    else:
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)


# 蔵元の選択
@app.route('/select_brewery', methods=['GET', 'POST'])
def select_brewery():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    input_brand = ""
    search_brands = apiget.search_brands(input_brand)
    if request.method == 'POST':
        if request.form['area'].isdecimal():
            area_id = int(request.form['area'])
        if request.form['brewery'].isdecimal():
            brewery_id = int(request.form['brewery'])
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)
    else:
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)

# 銘柄の選択
@app.route('/select_brand', methods=['GET', 'POST'])
def select_brand():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    input_brand = ""
    search_brands = apiget.search_brands(input_brand)
    if request.method == 'POST':
        if request.form['area'].isdecimal():
            area_id = int(request.form['area'])
        if request.form['brewery'].isdecimal():
            brewery_id = int(request.form['brewery'])
        if request.form['brand'].isdecimal():
            brand_id = int(request.form['brand'])
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        flavor = apiget.get_flavors(brand_id, brands)
        flavor_chart = fc.get_flavor_chart(flavor)
        flavor_tags = apiget.get_flavor_tags(brand_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand, flavor=flavor, flavor_chart=flavor_chart, flavor_tags=flavor_tags)
    else:
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)

# 絞り込み検索終わり

# 銘柄名検索
@app.route('/search_brand', methods=['GET', 'POST'])
def search_brand():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    selected_brand_id = ""
    if request.method == 'POST':
        input_brand = request.form['input_brand']
        search_brands = apiget.search_brands(input_brand)
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, selected_brand_id=selected_brand_id, search_brands=search_brands, input_brand=input_brand)
    else:
        input_brand = ""
        search_brands = apiget.search_brands(input_brand)
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)

@app.route('/select_search_brand', methods=['GET', 'POST'])
def select_search_brand():
    area_id = ""
    brewery_id = ""
    brand_id = ""
    selected_brand_id = ""
    if request.method == 'POST':
        input_brand = request.form['input_brand']
        search_brands = apiget.search_brands(input_brand)
        if request.form['selected_brand'].isdecimal():
            selected_brand_id = int(request.form['selected_brand'])
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        flavor = apiget.get_flavors(selected_brand_id, search_brands)
        flavor_chart = fc.get_flavor_chart(flavor)
        flavor_tags = apiget.get_flavor_tags(selected_brand_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands,area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, selected_brand_id=selected_brand_id, search_brands=search_brands, input_brand=input_brand, flavor=flavor, flavor_chart=flavor_chart, flavor_tags=flavor_tags)
    else:
        input_brand = ""
        search_brands = apiget.search_brands(input_brand)
        areas = apiget.get_area()
        breweries = apiget.get_breweries(area_id)
        brands = apiget.get_brands(brewery_id)
        return render_template('index.html',
                                areas=areas, breweries=breweries, brands=brands, area_id=area_id, brewery_id=brewery_id, brand_id=brand_id, search_brands=search_brands, input_brand=input_brand)


if __name__ == '__main__':
    app.run(host='0.0.0.0')