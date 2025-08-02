FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# 非rootユーザーを作成してセキュリティを向上
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Cloud Runのポート環境変数（通常8080）を使用
EXPOSE 8080

# アプリケーションを起動
CMD ["python", "main.py"]
