# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory product data
PRODUCTS = [
    {"id": 1, "name": "Laptop Pro X", "price": 1200.00, "inventory": 50},
    {"id": 2, "name": "Mechanical Keyboard", "price": 150.00, "inventory": 120},
    {"id": 3, "name": "Wireless Mouse", "price": 35.00, "inventory": 300}
]

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    # Adding a simple log message to check environment status
    print(f"INFO: Serving {len(PRODUCTS)} products.")
    return jsonify(PRODUCTS)

# Basic health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "product-catalog-service"}), 200

if __name__ == '__main__':
    # Running on port 5000 inside the Docker container
    app.run(host='0.0.0.0', port=5000)
