from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

productsUrl = 'https://fakestoreapi.com/products'
categoriesUrl = 'https://fakestoreapi.com/products/categories'

@app.route('/')
def home():
    resp = requests.get(url=productsUrl+'?limit=5')
    productsList = resp.json()

    resp = requests.get(url=categoriesUrl)
    categoriesList = resp.json()


    return render_template('homepage.html',
                           categoriesList=categoriesList,
                           productsList=productsList)
@app.route('/category/<selected_cat>')
def category(selected_cat):
    resp = requests.get(url=productsUrl + '/category/'+ selected_cat)
    productsList = resp.json()
    return render_template('category.html',
                           productsList=productsList,
                           selected_cat=selected_cat)

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port= 8090)
