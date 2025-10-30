#!/bin/bash
# start.sh — starts backend + frontend for Railway

# Navigate to backend and start the Flask API
cd backend
pip install -r requirements.txt
python app.py &
cd ..

# Navigate to frontend and start React
cd frontend
npm install
npm run build
npx serve -s build
