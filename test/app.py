
from flask import Flask, request
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

@app.route('/query-example')
def query_example():
   
    language = request.args.get('language')

    
    framework = request.args['framework']

   
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)



@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    
    currency = requests.form.get('currency')
    URL = 'https://coinmarketcap.com/currencies/' + currency + '/news/'
    r = request.get(URL, 'html.parser').text
    article = BeautifulSoup(r, 'lxml')

    if request.method == 'POST':
        currency = requests.form.get('currency')
        article
        return '''
                  <h1>The currency value is: {}</h1>
                  <h1>The article value is: {}</h1>'''.format(currency, article)

    
    return '''
           <form method="POST">
               <div><label>Currency: <input type="text" name="currency"></label></div>
               <input type="submit" value="Submit">
           </form>'''



@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)