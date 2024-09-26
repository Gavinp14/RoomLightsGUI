FROM python:3.9-slim
LABEL authors="gavpo"
WORKDIR /RoomLightsGUI
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "WakeupSleepLights.py"]
