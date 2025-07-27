#!/usr/bin/env python3
"""
Script tự động cài đặt Suna với thông tin đã có sẵn
"""
import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Chạy command và in output"""
    print(f"🔄 Đang chạy: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def main():
    print("""
🚀 SUNA AUTO SETUP
==================
Đang tự động cài đặt Suna với thông tin đã cung cấp...
""")
    
    # Kiểm tra thư mục hiện tại
    if not Path("backend").exists() or not Path("frontend").exists():
        print("❌ Vui lòng chạy script từ thư mục gốc của Suna")
        sys.exit(1)
    
    # 1. Cài đặt backend dependencies
    print("\n📦 Bước 1: Cài đặt Backend Dependencies")
    if not run_command("pip install uv", cwd="backend"):
        print("❌ Không thể cài đặt uv")
        return False
    
    if not run_command("uv sync", cwd="backend"):
        print("❌ Không thể cài đặt backend dependencies")
        return False
    
    # 2. Cài đặt frontend dependencies
    print("\n📦 Bước 2: Cài đặt Frontend Dependencies")
    if not run_command("npm install", cwd="frontend"):
        print("❌ Không thể cài đặt frontend dependencies")
        return False
    
    # 3. Tạo file cấu hình frontend
    print("\n⚙️ Bước 3: Tạo cấu hình Frontend")
    frontend_env = """NEXT_PUBLIC_APP_URL=https://work-1-dggeamiqbmqoxchl.prod-runtime.all-hands.dev
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL=https://hrgtaavhrqyjgeniqkjh.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhyZ3RhYXZocnF5amdlbmlxa2poIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2MTA3NDIsImV4cCI6MjA2OTE4Njc0Mn0.hymH7D9YvSBCoMmbPWLvYaowHj1R2ARoIfOlmMkj-2o
"""
    
    with open("frontend/.env.local", "w") as f:
        f.write(frontend_env)
    print("✅ Đã tạo file cấu hình frontend")
    
    # 4. Cài đặt Redis (nếu cần)
    print("\n🔧 Bước 4: Cài đặt Redis")
    run_command("apt-get update && apt-get install -y redis-server")
    
    # 5. Khởi chạy Redis
    print("\n🚀 Bước 5: Khởi chạy Redis")
    run_command("redis-server --daemonize yes")
    
    print("""
✅ CÀI ĐẶT HOÀN TẤT!
===================

Các bước tiếp theo:
1. Khởi chạy backend: cd backend && uv run uvicorn api:app --host 0.0.0.0 --port 8000
2. Khởi chạy frontend: cd frontend && npm run dev -- --port 12000 --hostname 0.0.0.0
3. Truy cập: https://work-1-dggeamiqbmqoxchl.prod-runtime.all-hands.dev

Hoặc sử dụng script khởi chạy tự động:
python start_services.py
""")

if __name__ == "__main__":
    main()