Setup:
Use python3}

pip install -r requirements.txt
export FLASK_APP=app.py
flask run 

APIs:
/api/product/product_id

{"name": "Metallic-Sky-Ring-Crossbody", "about": "Product Detail", "seller": "A Sellers", "price": 25}



/api/product-images/product_id

{"tile": "https://title-image", 
"medium": "https://medium-image", 
"big": "https://big-image"}



/api/product-recommendations/product_id

[{"id": 3, "name": "ABC", "title": "ABC Leather bag", "image": "https://title-image", "price": 45.5},
{"id": 4, "name": "XYZ", "title": "XYZ Light bag", "image": "https://title-image", "price": 50}]



/api/reviews/product_id

[{"reviewer": "Mr. A", "reviewed_at": "2018-10-26 10:00", "review": "Product is Good"}, 
{"reviewer": "Mr. B", "reviewed_at": "2018-10-26 10:00", "review": "Product is just fine, Not More."}]



/api/product-ads/product_id

[
    {
        "id": 5,
        "name": "Socks A",
        "title": "Nice Socks",
        "image": "https://title-image",
        "price": 100
    },
    {
        "id": 8,
        "name": "Purse B",
        "title": "Stylish Purse",
        "image": "https://title-image",
        "price": 40
    }
]



/api/edd
{
    "standard": "2018-11-02",
    "express": "2018-10-29"
}
