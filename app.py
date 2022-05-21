from flask import Flask
from flask import render_template
from flask import escape, request
from pydantic import BaseModel, validator

class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
    # Print the form data to the console
      for key, value in request.form.items():
          print(f'{key}: {value}')
          
      try:
          stock_data = StockModel(
              stock_symbol=request.form['stock_symbol'],
              number_of_shares=request.form['number_of_shares'],
              purchase_price=request.form['purchase_price']
          )
          print(stock_data_
     except ValidationError as e:
         print(e)

    return render_template('add_stock.html')

@app.route('/stocks/')
def stocks():
    return '<h2>Stock list ...</h2>'

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'
