# 1. 기본 이미지 설정 (가벼운 파이썬 이미지만 사용)
FROM python:3.10-alpine

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 호스트의 requirements.txt 를 컨테이너 안으로 복사하고 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 코드 (main.py) 를 컨테이너 안으로 복사
# 윈도우에서는 현재 폴더가 C:\Users\jhoon\workspace\homeLab\apps\my-web 이므로 
# 해당 경로에 main.py 가 있는지 확인해야 합니다.
COPY . . 

# 5. 포트 8000 에 대해 연결 가능하도록 설정
EXPOSE 8000

# 6. 서버 실행 명령어 설정 (--reload 은 개발용, 배포 시에는 --host 0.0.0.0 필수)
# 로컬 테스트용으로 reload 옵션 추가 (실제 운영은 --no-reload 권장)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]