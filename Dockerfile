# ใช้ Python เวอร์ชันล่าสุด (Slim ลดขนาด Image)
FROM python:3.9-slim

WORKDIR /app

# คัดลอก dependencies และติดตั้งก่อน
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดลง Container
COPY . .

# กำหนดให้ใช้ python3 เป็นค่าเริ่มต้น
CMD ["python3", "main.py"]
