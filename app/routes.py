from flask import render_template, flash, redirect
from app import app
from app.local_load import LocalLoadForm
from tasty_analyzer import transaction

# ...
@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Albert'}
  return render_template('index.html', title='Home', user=user)


@app.route('/local', methods=['GET', 'POST'])
def local():
  form = LocalLoadForm()
  if form.validate_on_submit():
        flash('Loading {}'.format(
            form.csv_path.data))
        return render_csv(form) 
  return render_template('local_load.html', title='Local CSV Load', form=form)
  
  
@app.route('/data')
def data():
   pass

# /Users/alberta/Developer/git/tasty_anaylzer/real_data/tastyworks_transactions_x6557_2017-01-01_2018-05-14.csv 
def render_csv(form):
   transaction_map = transaction.build_transaction_map(form.csv_path.data)
   return render_template('transactions.html', data = transaction_map) 
  




    