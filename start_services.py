#!/usr/bin/env python3
"""
Script khởi chạy tất cả services của Suna
"""
import os
import subprocess
import time
import signal
import sys
from pathlib import Path

def start_service(name, cmd, cwd=None, log_file=None):
    """Khởi chạy một service trong background"""
    print(f"🚀 Đang khởi chạy {name}...")
    
    if log_file:
        with open(log_file, "w") as f:
            process = subprocess.Popen(
                cmd, shell=True, cwd=cwd,
                stdout=f, stderr=subprocess.STDOUT
            )
    else:
        process = subprocess.Popen(
            cmd, shell=True, cwd=cwd,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    
    return process

def main():
    print("""
🌟 SUNA SERVICES LAUNCHER
=========================
Đang khởi chạy tất cả services...
""")
    
    processes = []
    
    try:
        # 1. Khởi chạy Redis
        print("📦 Khởi chạy Redis...")
        redis_process = start_service("Redis", "redis-server", log_file="/tmp/redis.log")
        processes.append(("Redis", redis_process))
        time.sleep(2)
        
        # 2. Khởi chạy Backend
        print("🔧 Khởi chạy Backend API...")
        backend_process = start_service(
            "Backend", 
            "uv run uvicorn api:app --host 0.0.0.0 --port 8000",
            cwd="backend",
            log_file="/tmp/backend.log"
        )
        processes.append(("Backend", backend_process))
        time.sleep(5)
        
        # 3. Khởi chạy Frontend
        print("🌐 Khởi chạy Frontend...")
        frontend_process = start_service(
            "Frontend",
            "npm run dev -- --port 12000 --hostname 0.0.0.0",
            cwd="frontend",
            log_file="/tmp/frontend.log"
        )
        processes.append(("Frontend", frontend_process))
        
        print("""
✅ TẤT CẢ SERVICES ĐÃ KHỞI CHẠY!
===============================

🌐 Frontend: https://work-1-dggeamiqbmqoxchl.prod-runtime.all-hands.dev
🔧 Backend API: http://localhost:8000
📦 Redis: localhost:6379

📋 Logs:
- Redis: /tmp/redis.log
- Backend: /tmp/backend.log  
- Frontend: /tmp/frontend.log

Nhấn Ctrl+C để dừng tất cả services...
""")
        
        # Chờ và giữ cho processes chạy
        while True:
            time.sleep(1)
            # Kiểm tra xem có process nào bị dừng không
            for name, process in processes:
                if process.poll() is not None:
                    print(f"⚠️ {name} đã dừng!")
    
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng tất cả services...")
        
        for name, process in processes:
            print(f"🔄 Đang dừng {name}...")
            try:
                process.terminate()
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            print(f"✅ Đã dừng {name}")
        
        print("✅ Đã dừng tất cả services!")

if __name__ == "__main__":
    main()