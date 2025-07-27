#!/usr/bin/env python3
"""
Test Setup Script - Kiểm tra cài đặt Suna
"""
import os
import subprocess
import sys
from pathlib import Path

def check_command(cmd, name):
    """Kiểm tra xem command có tồn tại không"""
    try:
        result = subprocess.run(f"which {cmd}", shell=True, capture_output=True)
        if result.returncode == 0:
            print(f"✅ {name} đã được cài đặt")
            return True
        else:
            print(f"❌ {name} chưa được cài đặt")
            return False
    except:
        print(f"❌ Không thể kiểm tra {name}")
        return False

def check_file(filepath, name):
    """Kiểm tra xem file có tồn tại không"""
    if Path(filepath).exists():
        print(f"✅ {name} tồn tại")
        return True
    else:
        print(f"❌ {name} không tồn tại")
        return False

def check_port(port, name):
    """Kiểm tra xem port có đang được sử dụng không"""
    try:
        result = subprocess.run(f"lsof -i:{port}", shell=True, capture_output=True)
        if result.returncode == 0:
            print(f"✅ {name} đang chạy trên port {port}")
            return True
        else:
            print(f"❌ {name} không chạy trên port {port}")
            return False
    except:
        print(f"❌ Không thể kiểm tra port {port}")
        return False

def main():
    print("""
🔍 SUNA SETUP TEST
==================
Kiểm tra cài đặt và cấu hình...
""")
    
    # Kiểm tra requirements
    print("📋 Kiểm tra System Requirements:")
    check_command("python3", "Python 3")
    check_command("node", "Node.js")
    check_command("npm", "NPM")
    check_command("git", "Git")
    check_command("redis-server", "Redis")
    
    print("\n📁 Kiểm tra Project Structure:")
    check_file("backend", "Backend directory")
    check_file("frontend", "Frontend directory")
    check_file("backend/pyproject.toml", "Backend config")
    check_file("frontend/package.json", "Frontend config")
    
    print("\n⚙️ Kiểm tra Configuration Files:")
    check_file(".env.example", "Environment template")
    check_file("frontend/.env.example", "Frontend template")
    check_file("quick_setup.py", "Quick setup script")
    check_file("start_services.py", "Service launcher")
    
    print("\n🔧 Kiểm tra Dependencies:")
    
    # Backend dependencies
    try:
        result = subprocess.run("cd backend && uv --version", shell=True, capture_output=True)
        if result.returncode == 0:
            print("✅ UV package manager")
        else:
            print("❌ UV package manager")
    except:
        print("❌ UV package manager")
    
    # Frontend dependencies
    if Path("frontend/node_modules").exists():
        print("✅ Frontend dependencies")
    else:
        print("❌ Frontend dependencies")
    
    print("\n🚀 Kiểm tra Services:")
    check_port(6379, "Redis")
    check_port(8000, "Backend API")
    check_port(3000, "Frontend")
    
    print("\n📝 Kiểm tra Environment Files:")
    if Path(".env").exists():
        print("✅ Backend environment file (.env)")
    else:
        print("⚠️ Backend environment file (.env) - Cần tạo từ .env.example")
    
    if Path("frontend/.env.local").exists():
        print("✅ Frontend environment file (.env.local)")
    else:
        print("⚠️ Frontend environment file (.env.local) - Cần tạo từ .env.example")
    
    print("""
📋 HƯỚNG DẪN TIẾP THEO:
======================

Nếu có lỗi ❌, hãy:
1. Cài đặt missing requirements
2. Chạy: python quick_setup.py
3. Tạo file .env từ .env.example
4. Chạy: python start_services.py

Nếu tất cả ✅:
🎉 Suna đã sẵn sàng sử dụng!
""")

if __name__ == "__main__":
    main()