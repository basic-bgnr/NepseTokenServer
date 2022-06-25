#!/bin/bash
export FLASK_APP=NepseTokenServer
export FLASK_ENV=development
export FLASK_RUN_PORT=4000
flask run --with-threads
