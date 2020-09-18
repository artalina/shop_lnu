from flask import Flask
from datetime import datetime
from flask import render_template
  
app = Flask(__name__) 


  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Geeks for Geeks SHOP_lnu</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




