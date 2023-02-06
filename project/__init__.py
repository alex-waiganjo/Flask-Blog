from flask import Flask
from project.config import Config

app = Flask(__name__)
app.config.from_object(Config)

