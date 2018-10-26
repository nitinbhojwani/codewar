from datetime import datetime
from flask import Flask, request, Response
import json

from utils import cal_delivery_date

app = Flask(__name__)

@app.route('/api/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = {
        'name': 'Metallic-Sky-Ring-Crossbody',
        'about': 'Product Detail',
        'seller': 'A Sellers',
        'price': 25,
    }
    return Response(json.dumps(product), status=200, mimetype='application/json')

@app.route('/api/product-images/<product_id>', methods=['GET'])
def get_product_images(product_id):
    images = {'tile': 'https://title-image' , 'medium': 'https://medium-image' , 'big': 'https://big-image'}
    return Response(json.dumps(images), status=200, mimetype='application/json')


@app.route('/api/product-recommendations/<product_id>', methods=['GET'])
def get_recommendations(product_id):
    recommended_products = [
        {'id': 3, 'name': 'ABC', 'title': 'ABC Leather bag','image': 'https://title-image','price': 45.5},
        {'id': 4, 'name': 'XYZ', 'title': 'XYZ Light bag','image': 'https://title-image','price': 50}
        ]

    return Response(json.dumps(recommended_products), status=200, mimetype='application/json')

@app.route('/api/reviews/<product_id>', methods=['GET'])
def get_reviews(product_id):
    res = [
        {'reviewer': 'Mr. A', 'reviewed_at':'2018-10-26 10:00', 'review': 'Product is Good'},
        {'reviewer': 'Mr. B', 'reviewed_at':'2018-10-26 10:00', 'review': 'Product is just fine, Not More.'}
    ]
    return Response(json.dumps(res), status=200, mimetype='application/json')


@app.route('/api/product-ads/<product_id>', methods=['GET'])
def get_ads(product_id):
    similar_sponsored_products = [
       {'id': 5, 'name': 'Socks A', 'title': 'Nice Socks','image': 'https://title-image','price': 100},
       {'id': 8, 'name': 'Purse B', 'title': 'Stylish Purse','image': 'https://title-image','price': 40}
    ]

    return Response(json.dumps(similar_sponsored_products), status=200, mimetype='application/json')



@app.route('/api/edd')
def get_estimated_delivery_date():
    try:
        date = datetime.strptime(request.args.get('date'), '%Y-%m-%d')
    except:
        return Response(json.dumps({'error': 'invalid or no date provided'}), status=400, mimetype='application/json')

    standard_delivery_date = cal_delivery_date('standard', date.date())
    express_delivery_date = cal_delivery_date('express', date.date())

    res = {
        'standard': standard_delivery_date.strftime('%Y-%m-%d'),
        'express': express_delivery_date.strftime('%Y-%m-%d')
    }
    
    return Response(json.dumps(res), status=200, mimetype='application/json')
