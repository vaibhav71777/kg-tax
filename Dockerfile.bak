# Use Node with Python preinstalled
FROM node:18-bullseye

# Set workdir
WORKDIR /app

# --- Backend setup ---
COPY backend ./backend
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r backend/requirements.txt

# --- Frontend setup ---
COPY frontend ./frontend
WORKDIR /app/frontend
RUN npm install
RUN npm run build

# --- Serve built frontend via Flask backend ---
WORKDIR /app/backend
COPY backend/app.py .

# Flask listens on port 5000
EXPOSE 5000

CMD ["python3", "app.py"]
