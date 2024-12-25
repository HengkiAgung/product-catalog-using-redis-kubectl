import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Menghubungkan ke Redis (sesuaikan dengan nama service Redis di Kubernetes)
# redis_client = redis.StrictRedis(host='redis', port=6379, db=0, password='your-secure-password')
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Simulasi data katalog produk
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
    {"id": 3, "name": "Headphones", "price": 200},
]

@app.route('/products', methods=['GET'])
def get_products():
    # Cek apakah data produk sudah ada di Redis cache
    cached_products = redis_client.get('products')
    
    if cached_products:
        # Jika data ada di cache, kembalikan data dari cache
        return jsonify({"source": "cache", "data": eval(cached_products.decode('utf-8'))})
    
    # Jika data tidak ada di cache, ambil data produk dari database atau sumber utama
    # Simulasi menyimpan data ke Redis cache untuk penggunaan berikutnya
    redis_client.set('products', str(PRODUCTS))  # Menyimpan data produk dalam cache Redis
    
    return jsonify({"source": "db", "data": PRODUCTS})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
