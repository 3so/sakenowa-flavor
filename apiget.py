import requests
import json

urls = {
    "地域一覧": "https://muro.sakenowa.com/sakenowa-data/api/areas",
    "銘柄一覧": "https://muro.sakenowa.com/sakenowa-data/api/brands",
    "蔵元一覧": "https://muro.sakenowa.com/sakenowa-data/api/breweries",
    "ランキング": "https://muro.sakenowa.com/sakenowa-data/api/rankings",
    "フレーバーチャート": "https://muro.sakenowa.com/sakenowa-data/api/flavor-charts",
    "フレーバータグ": "https://muro.sakenowa.com/sakenowa-data/api/flavor-tags",
    "銘柄ごとフレーバータグ": "https://muro.sakenowa.com/sakenowa-data/api/brand-flavor-tags",
    }

def get_area():
    url = urls["地域一覧"]
    responce_areas = requests.get(url).json()
    return responce_areas["areas"]

def get_breweries(area_id):
    url = urls["蔵元一覧"]
    responce_breweries = requests.get(url).json()
    breweries = responce_breweries["breweries"]
    selected_breweries = []
    for brewery in breweries:
        if brewery["areaId"] == area_id and brewery["name"] != "":
            selected_breweries.append(brewery)
    if selected_breweries == []:
        return [{"id":"","name":"------","areaId":""}]
    else:
        selected_breweries.insert(0, {"id":"","name":"選択してください","areaId":""})
        return selected_breweries

def get_brands(brewery_id):
    url = urls["銘柄一覧"]
    responce_brands = requests.get(url).json()
    brands = responce_brands["brands"]
    selected_brands = []
    for brand in brands:
        if brand["breweryId"] == brewery_id:
            selected_brands.append(brand)
    if selected_brands == []:
        return [{"id":"","name":"------","breweryId":""}]
    else:
        selected_brands.insert(0, {"id":"","name":"選択してください","breweryId":""})
        return selected_brands

def get_fravors(brand_id):
    url = urls["フレーバーチャート"]
    responce_fravor_charts = requests.get(url).json()
    flavor_charts = responce_fravor_charts["flavorChart"]
    for flavor_chart in flavor_charts:
        if flavor_chart["brandId"] == brand_id:
            return flavor_chart["brandId"]
    return {}