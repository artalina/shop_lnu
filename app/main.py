from flask import Flask
from datetime import datetime
from flask import render_template
from shop_lnu import app 
  
app = Flask(__name__) 


  
@app.route("/") 
#def home_view(): 
#        return "<h1>Welcome to Geeks for Geeks</h1>"

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )



