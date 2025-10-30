# Base image with both Node and Python
FROM node:18-bullseye

# Set workdir
WORKDIR /app

# Copy backend
COPY backend ./backend
WORKDIR /app/backend
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# Copy frontend
WORKDIR /app/frontend
COPY frontend ./frontend
RUN npm install && npm run build

# Serve frontend and backend
WORKDIR /app
COPY backend/app.py .
EXPOSE 5000

CMD python3 backend/app.py
