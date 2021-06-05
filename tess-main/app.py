import os, sys
from flask import Flaskimport views

app = Flask(__name__)
app.add_url_rule("/", view_func = views.root, methods=['GET'])
app.add_url_rule("/read_ocr", view_func = views.read_ocr, methods=['POST'])
print("Server Ready", flush=True)

if __name__ == "__main__":    
  app.run(host='0.0.0.0', port=4000)
