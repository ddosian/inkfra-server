from utils import *

import database
from flask import Flask

log.debug(database.execute("SELECT version()"))

database.initialize()

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return "Service is running!"

@app.route('/devices/get', methods=['GET'])
def get_devices():
    try:
        devices = database.execute("SELECT * FROM devices")
        return {"devices": devices}, 200
    except Exception as e:
        log.error(f"Error fetching devices: {e}")
        return {"error": "Unable to fetch devices"}, 500

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')