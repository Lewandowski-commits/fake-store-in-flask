from flask import Flask, render_template, url_for
from random import sample
import requests

app = Flask(__name__)

productsUrl = 'https://fakestoreapi.com/products'
categoriesUrl = 'https://fakestoreapi.com/products/categories'

def get_resp_json(url:str):
    '''
    Takes a single url and returns the json content of the reply.
    :param url:
    :return:
    '''
    resp = requests.get(url=url)
    result = resp.json()
    return result


@app.route('/')
def home():
    productsListPreSel = get_resp_json(productsUrl)
    productsList = sample(productsListPreSel, 3)

    categoriesList = get_resp_json(categoriesUrl)

    return render_template('homepage.html',
                           categoriesList=categoriesList,
                           productsList=productsList)


@app.route('/category/<selected_cat>')
def category(selected_cat):
    productsList = get_resp_json(productsUrl + '/category/' + selected_cat)
    return render_template('category.html',
                           productsList=productsList,
                           selected_cat=selected_cat)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=8090)
