README - Telegram Bot Render Deployment Guide

1. Make sure all files (main.py, config.py, qr_code.png, requirements.txt, runtime.txt) are in the root directory (NOT inside /src).

2. Render Deployment:
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py

3. If you placed files inside a folder like /src, update Start Command to: python src/main.py
