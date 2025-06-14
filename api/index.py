import sys
import os
from flask import Flask, request

# 프로젝트 루트 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Flask 앱 import
try:
    from app import app
except ImportError as e:
    print(f"Import error: {e}")
    # 기본 Flask 앱 생성 (fallback)
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return f"Import Error: {str(e)}"

# Vercel serverless function handler
def handler(request, context):
    """Vercel serverless function handler"""
    with app.app_context():
        return app.full_dispatch_request() 