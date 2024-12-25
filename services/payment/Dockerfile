# Gunakan image dasar Python
FROM python:3.9-slim

# Atur direktori kerja di dalam kontainer
WORKDIR /app

# Salin file requirements.txt ke direktori kerja
COPY app/requirements.txt .

# Instal semua dependensi Python dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instal library tracing tambahan
RUN pip install jaeger-client flask-opentracing

# Salin semua file dari folder app ke dalam kontainer
COPY app/ .

# Jalankan aplikasi
CMD ["python", "main.py"]
