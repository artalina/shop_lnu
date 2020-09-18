from flask import Flask
from datetime import datetime
from flask import render_template
  
app = Flask(__name__) 


  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Geeks for Geeks SHOP_lnu</h1>"




