from utils import *

import database
from flask import Flask

postgres_version = database.execute("SELECT version()")[0][0].split(" ")[1]

database.initialize()

app = Flask(__name__)

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return {"status": "Service is running!", "postgres_version": postgres_version}, 200

@app.route('/api/v1/devices/get', methods=['GET'])
def get_devices():
    try:
        devices = database.execute("SELECT * FROM devices")
        return {"devices": devices}, 200
    except Exception as e:
        log.error(f"Error fetching devices: {e}")
        return {"error": "Unable to fetch devices"}, 500

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')