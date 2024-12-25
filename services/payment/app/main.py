import redis
from flask import Flask, jsonify, request

app = Flask(__name__)

# Menghubungkan ke Redis (sesuaikan dengan nama service Redis di Kubernetes)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/payment', methods=['POST'])
def process_payment():
    # Ambil data pembayaran dari request
    payment_data = request.json
    user_id = payment_data.get('user_id')
    amount = payment_data.get('amount')

    # Simulasi memproses pembayaran
    payment_status = {"status": "success", "amount": amount}

    # Menyimpan status pembayaran di Redis
    redis_client.set(f'payment:user:{user_id}', str(payment_status))
    
    return jsonify({"message": "Payment processed successfully", "payment_status": payment_status})

@app.route('/payment/status/<user_id>', methods=['GET'])
def get_payment_status(user_id):
    # Mengambil status pembayaran dari Redis
    payment_status = redis_client.get(f'payment:user:{user_id}')
    
    if payment_status:
        return jsonify({"source": "cache", "user_id": user_id, "payment_status": eval(payment_status.decode('utf-8'))})
    
    return jsonify({"message": "Payment status not found", "status": "failed"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
