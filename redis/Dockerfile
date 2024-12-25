# Gunakan Redis image resmi dari Docker Hub
FROM redis:latest

# Salin konfigurasi Redis dari direktori lokal ke dalam kontainer
COPY redis.conf /usr/local/etc/redis/redis.conf

# Jalankan Redis dengan konfigurasi custom
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
