from flask import Flask

app = Flask(__name__)

@app.route("/")

 

def main():
  return "WIN_20190722_11_13_09_Pro.jpg"
  
 
 
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  app.run(debug=True)
