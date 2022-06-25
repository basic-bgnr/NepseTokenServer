import flask
from flask import Flask, request

from NepseTokenManager import NepseTokenManager

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

nepse_token_manager = NepseTokenManager()


@app.route("/")
def getIndex():
    return nepse_token_manager.getValidToken()