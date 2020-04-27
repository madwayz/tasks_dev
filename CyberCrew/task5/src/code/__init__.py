from flask import Flask
import os

app = Flask(__name__, static_url_path='')

FLAG = os.environ.get('FLAG')

import code.routes




