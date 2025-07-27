#!/usr/bin/env python3
"""
Quick Setup Script for Suna
Tự động cài đặt và cấu hình Suna với API keys có sẵn
"""
import os
import subprocess
import sys
import shutil
from pathlib import Path

# API Keys - Thay thế bằng keys thật của bạn
API_KEYS = {
    'ENCRYPTION_KEY': 'Wg9QjA-8IwjWutsgFjoW5tgf77UiHELTEvppzCEgmhc=',
    # Supabase (Required)
    "SUPABASE_URL": "https://hrgtaavhrqyjgeniqkjh.supabase.co",
    "SUPABASE_ANON_KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhyZ3RhYXZocnF5amdlbmlxa2poIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2MTA3NDIsImV4cCI6MjA2OTE4Njc0Mn0.hymH7D9YvSBCoMmbPWLvYaowHj1R2ARoIfOlmMkj-2o",
    "SUPABASE_SERVICE_ROLE_KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhyZ3RhYXZocnF5amdlbmlxa2poIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzYxMDc0MiwiZXhwIjoyMDY5MTg2NzQyfQ.cbFDeu_59P144qnCtX9cfty6QFe_28j7mfxUkmFDl30",
    
    # AI Services
    "DAYTONA_API_KEY": "dtn_6d89b45115be2b936ba576bc4d632024bc6b9e0cc818712724904447ec463bdc",
    "MORPH_API_KEY": "sk-A7JwiFcalpLwNsaiwNY4vi60ysSgzgHQeCwbxwXynp2jhH-9",
    
    # Search & Scraping
    "TAVILY_API_KEY": "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",
    "FIRECRAWL_API_KEY": "fc-5baae9da61f944159adc0ef085f38161",
    
    # Background Jobs
    "QSTASH_URL": "https://qstash.upstash.io",
    "QSTASH_TOKEN": "eyJVc2VySUQiOiI5YWNiZjc4NS1mOGYxLTQ0YTQtYWZjOC1hYjA1N2Q5MzBiZjkiLCJQYXNzd29yZCI6IjNjYTE2OTE3NjVhODQ5NTRiNjM3YTc2M2E2NGRiMTc3In0=",
    "QSTASH_CURRENT_SIGNING_KEY": "sig_5RAHirfXnUV4RSoWpKVL4em4GycQ",
    "QSTASH_NEXT_SIGNING_KEY": "sig_7q2Z2cWdV6Yu6yugaZYYerTjjM4K",
    
    # Tunneling
    "NGROK_AUTHTOKEN": "30SZigwTcVVKPWUMrx0JgbUlnbZ_5xHjoS1ZSpqX7fGLXH7up",
}

def run_command(cmd, cwd=None, show_output=True):
    """Chạy command và trả về kết quả"""
    if show_output:
        print(f"🔄 {cmd}")
    
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, check=True,
            capture_output=not show_output, text=True
        )
        return True, result.stdout if not show_output else ""
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi: {e}")
        return False, e.stderr if hasattr(e, 'stderr') else str(e)

def create_env_files():
    """Tạo các file environment với API keys"""
    print("📝 Tạo file cấu hình...")
    
    # Tạo .env cho backend
    env_content = f"""# Suna Configuration - Auto Generated
NODE_ENV=development
NEXT_PUBLIC_APP_URL=http://localhost:3000
API_URL=http://localhost:8000

# Supabase Configuration
SUPABASE_URL={API_KEYS['SUPABASE_URL']}
SUPABASE_ANON_KEY={API_KEYS['SUPABASE_ANON_KEY']}
SUPABASE_SERVICE_ROLE_KEY={API_KEYS['SUPABASE_SERVICE_ROLE_KEY']}

# AI Services
DAYTONA_API_KEY={API_KEYS['DAYTONA_API_KEY']}
MORPH_API_KEY={API_KEYS['MORPH_API_KEY']}

# Search and Crawling
TAVILY_API_KEY={API_KEYS['TAVILY_API_KEY']}
FIRECRAWL_API_KEY={API_KEYS['FIRECRAWL_API_KEY']}

# Background Jobs
QSTASH_URL={API_KEYS['QSTASH_URL']}
QSTASH_TOKEN={API_KEYS['QSTASH_TOKEN']}
QSTASH_CURRENT_SIGNING_KEY={API_KEYS['QSTASH_CURRENT_SIGNING_KEY']}
QSTASH_NEXT_SIGNING_KEY={API_KEYS['QSTASH_NEXT_SIGNING_KEY']}

# Tunneling
NGROK_AUTHTOKEN={API_KEYS['NGROK_AUTHTOKEN']}

# Redis
REDIS_URL=redis://localhost:6379
REDIS_HOST=localhost
REDIS_PORT=6379
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    # Tạo .env.local cho frontend
    frontend_env = f"""# Frontend Configuration - Auto Generated
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL={API_KEYS['SUPABASE_URL']}
NEXT_PUBLIC_SUPABASE_ANON_KEY={API_KEYS['SUPABASE_ANON_KEY']}
"""
    
    with open("frontend/.env.local", "w") as f:
        f.write(frontend_env)
    
    print("✅ Đã tạo file cấu hình")

def install_dependencies():
    """Cài đặt dependencies"""
    print("📦 Cài đặt dependencies...")
    
    # Backend
    print("🔧 Backend dependencies...")
    success, _ = run_command("pip install uv", cwd="backend", show_output=False)
    if not success:
        return False
    
    success, _ = run_command("uv sync", cwd="backend")
    if not success:
        return False
    
    # Frontend
    print("🌐 Frontend dependencies...")
    success, _ = run_command("npm install", cwd="frontend")
    if not success:
        return False
    
    return True

def setup_redis():
    """Cài đặt và khởi chạy Redis"""
    print("📦 Cài đặt Redis...")
    
    # Kiểm tra xem Redis đã được cài chưa
    success, _ = run_command("which redis-server", show_output=False)
    if not success:
        print("🔄 Cài đặt Redis...")
        success, _ = run_command("apt-get update && apt-get install -y redis-server")
        if not success:
            print("⚠️ Không thể cài đặt Redis, bỏ qua...")
            return False
    
    # Khởi chạy Redis
    print("🚀 Khởi chạy Redis...")
    success, _ = run_command("redis-server --daemonize yes", show_output=False)
    return success

def main():
    print("""
🚀 SUNA QUICK SETUP
===================
Tự động cài đặt Suna với API keys có sẵn
""")
    
    # Kiểm tra thư mục
    if not Path("backend").exists() or not Path("frontend").exists():
        print("❌ Vui lòng chạy từ thư mục gốc của Suna")
        sys.exit(1)
    
    # Tạo file cấu hình
    create_env_files()
    
    # Cài đặt dependencies
    if not install_dependencies():
        print("❌ Không thể cài đặt dependencies")
        sys.exit(1)
    
    # Setup Redis
    setup_redis()
    
    print("""
✅ CÀI ĐẶT HOÀN TẤT!
===================

🚀 Khởi chạy services:
python start_services.py

🌐 Hoặc khởi chạy thủ công:
1. Backend: cd backend && uv run uvicorn api:app --host 0.0.0.0 --port 8000
2. Frontend: cd frontend && npm run dev -- --port 3000

📋 Logs sẽ được lưu tại:
- /tmp/backend.log
- /tmp/frontend.log
- /tmp/redis.log
""")

if __name__ == "__main__":
    main()