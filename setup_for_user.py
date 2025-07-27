#!/usr/bin/env python3
"""
Setup Script cho User - Cài đặt Suna cho người dùng cuối
"""
import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def print_header():
    print("🚀 SUNA SETUP - CÀI ĐẶT TỰ ĐỘNG")
    print("=" * 50)
    print("Đang cài đặt Suna AI Agent trên máy của bạn...")
    print()

def check_python():
    """Kiểm tra Python version"""
    print("🐍 Kiểm tra Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Cần Python 3.8+ để chạy Suna")
        print(f"   Phiên bản hiện tại: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_node():
    """Kiểm tra Node.js"""
    print("📦 Kiểm tra Node.js...")
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Node.js {version}")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ Node.js không được tìm thấy")
    print("   Vui lòng cài đặt Node.js từ: https://nodejs.org")
    return False

def check_redis():
    """Kiểm tra Redis"""
    print("🔴 Kiểm tra Redis...")
    try:
        result = subprocess.run(['redis-cli', 'ping'], capture_output=True, text=True)
        if result.returncode == 0 and 'PONG' in result.stdout:
            print("✅ Redis đang chạy")
            return True
    except FileNotFoundError:
        pass
    
    print("⚠️  Redis chưa chạy hoặc chưa cài đặt")
    return install_redis()

def install_redis():
    """Cài đặt Redis"""
    system = platform.system().lower()
    
    if system == "darwin":  # macOS
        print("🍎 Cài đặt Redis trên macOS...")
        try:
            subprocess.run(['brew', 'install', 'redis'], check=True)
            subprocess.run(['brew', 'services', 'start', 'redis'], check=True)
            print("✅ Redis đã được cài đặt và khởi chạy")
            return True
        except:
            print("❌ Không thể cài đặt Redis. Vui lòng cài đặt Homebrew trước")
            return False
    
    elif system == "linux":
        print("🐧 Cài đặt Redis trên Linux...")
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'redis-server'], check=True)
            subprocess.run(['sudo', 'systemctl', 'start', 'redis-server'], check=True)
            subprocess.run(['sudo', 'systemctl', 'enable', 'redis-server'], check=True)
            print("✅ Redis đã được cài đặt và khởi chạy")
            return True
        except:
            print("❌ Không thể cài đặt Redis. Vui lòng cài đặt thủ công")
            return False
    
    else:  # Windows
        print("🪟 Trên Windows, vui lòng cài đặt Redis thủ công:")
        print("   1. Tải Redis từ: https://redis.io/download")
        print("   2. Hoặc sử dụng WSL2 với Ubuntu")
        return False

def install_uv():
    """Cài đặt uv package manager"""
    print("📦 Cài đặt uv package manager...")
    try:
        if platform.system().lower() == "windows":
            subprocess.run(['powershell', '-c', 'irm https://astral.sh/uv/install.ps1 | iex'], check=True)
        else:
            subprocess.run(['curl', '-LsSf', 'https://astral.sh/uv/install.sh'], stdout=subprocess.PIPE, check=True)
            subprocess.run(['sh'], input=subprocess.PIPE, check=True)
        print("✅ uv đã được cài đặt")
        return True
    except:
        print("⚠️  Không thể cài đặt uv tự động")
        print("   Vui lòng cài đặt thủ công từ: https://astral.sh/uv/")
        return False

def setup_backend():
    """Cài đặt backend dependencies"""
    print("🔧 Cài đặt backend dependencies...")
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Thư mục backend không tồn tại")
        return False
    
    try:
        os.chdir(backend_dir)
        subprocess.run(['uv', 'sync'], check=True)
        os.chdir('..')
        print("✅ Backend dependencies đã được cài đặt")
        return True
    except:
        print("❌ Lỗi khi cài đặt backend dependencies")
        return False

def setup_frontend():
    """Cài đặt frontend dependencies"""
    print("🎨 Cài đặt frontend dependencies...")
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Thư mục frontend không tồn tại")
        return False
    
    try:
        os.chdir(frontend_dir)
        subprocess.run(['npm', 'install'], check=True)
        os.chdir('..')
        print("✅ Frontend dependencies đã được cài đặt")
        return True
    except:
        print("❌ Lỗi khi cài đặt frontend dependencies")
        return False

def setup_env_files():
    """Tạo file cấu hình"""
    print("⚙️  Tạo file cấu hình...")
    
    # Copy .env.example to .env
    if Path(".env.example").exists() and not Path(".env").exists():
        shutil.copy(".env.example", ".env")
        print("✅ Đã tạo file .env")
    
    # Copy frontend env
    frontend_env_example = Path("frontend/.env.example")
    frontend_env_local = Path("frontend/.env.local")
    if frontend_env_example.exists() and not frontend_env_local.exists():
        shutil.copy(frontend_env_example, frontend_env_local)
        print("✅ Đã tạo file frontend/.env.local")
    
    return True

def show_next_steps():
    """Hiển thị các bước tiếp theo"""
    print("\n🎉 CÀI ĐẶT HOÀN TẤT!")
    print("=" * 50)
    print("Các bước tiếp theo:")
    print()
    print("1. 🔑 Cập nhật API keys trong file .env:")
    print("   - SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY")
    print("   - MORPH_API_KEY (cho LLM)")
    print("   - TAVILY_API_KEY (cho web search)")
    print("   - FIRECRAWL_API_KEY (cho web scraping)")
    print()
    print("2. 🚀 Khởi chạy Suna:")
    print("   python start_services.py")
    print()
    print("3. 🌐 Truy cập ứng dụng:")
    print("   Frontend: http://localhost:3000")
    print("   Backend API: http://localhost:8000")
    print("   API Docs: http://localhost:8000/docs")
    print()
    print("📖 Xem thêm hướng dẫn trong file QUICK_START_VI.md")
    print()

def main():
    print_header()
    
    # Kiểm tra requirements
    if not check_python():
        sys.exit(1)
    
    if not check_node():
        sys.exit(1)
    
    redis_ok = check_redis()
    
    # Cài đặt uv nếu chưa có
    try:
        subprocess.run(['uv', '--version'], capture_output=True, check=True)
        print("✅ uv đã được cài đặt")
    except:
        if not install_uv():
            print("❌ Không thể cài đặt uv. Vui lòng cài đặt thủ công")
            sys.exit(1)
    
    # Cài đặt dependencies
    if not setup_backend():
        sys.exit(1)
    
    if not setup_frontend():
        sys.exit(1)
    
    # Tạo file cấu hình
    setup_env_files()
    
    # Hiển thị bước tiếp theo
    show_next_steps()

if __name__ == "__main__":
    main()