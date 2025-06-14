import sys
import os

# 프로젝트 루트 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Flask 앱 import
from app import app

# Vercel은 이 파일을 직접 실행하므로 app을 export
# 이것이 Vercel의 표준 방식입니다 