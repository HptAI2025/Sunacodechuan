#!/usr/bin/env python3
"""
Fix Configuration Script - Sửa lỗi cấu hình
"""
import os
from cryptography.fernet import Fernet

def generate_encryption_key():
    """Tạo encryption key mới"""
    return Fernet.generate_key().decode()

def update_env_files():
    """Cập nhật tất cả file cấu hình"""
    
    # Tạo encryption key
    encryption_key = generate_encryption_key()
    
    # Các biến cần thiết
    required_vars = {
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': '6379', 
        'DAYTONA_SERVER_URL': 'https://api.daytona.io',
        'DAYTONA_TARGET': 'default',
        'RAPID_API_KEY': 'dummy_rapid_api_key',
        'ENCRYPTION_KEY': encryption_key
    }
    
    # Cập nhật .env
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            content = f.read()
        
        for var, value in required_vars.items():
            if var not in content:
                content += f"\n{var}={value}"
        
        with open('.env', 'w') as f:
            f.write(content)
        print("✅ Đã cập nhật .env")
    
    # Cập nhật .env.example
    if os.path.exists('.env.example'):
        with open('.env.example', 'r') as f:
            content = f.read()
        
        additions = """
# Additional Required Fields
REDIS_HOST=localhost
REDIS_PORT=6379
DAYTONA_SERVER_URL=https://api.daytona.io
DAYTONA_TARGET=default
RAPID_API_KEY=your_rapid_api_key_here
ENCRYPTION_KEY=your_encryption_key_here
"""
        
        if 'REDIS_HOST' not in content:
            content += additions
        
        with open('.env.example', 'w') as f:
            f.write(content)
        print("✅ Đã cập nhật .env.example")
    
    # Cập nhật quick_setup.py
    if os.path.exists('quick_setup.py'):
        with open('quick_setup.py', 'r') as f:
            content = f.read()
        
        # Thêm encryption key vào API_KEYS
        if 'ENCRYPTION_KEY' not in content:
            content = content.replace(
                "API_KEYS = {",
                f"API_KEYS = {{\n    'ENCRYPTION_KEY': '{encryption_key}',"
            )
        
        # Thêm các biến vào template
        additions = f"""
# Additional Required Fields
REDIS_HOST=localhost
REDIS_PORT=6379
DAYTONA_SERVER_URL=https://api.daytona.io
DAYTONA_TARGET=default
RAPID_API_KEY=dummy_rapid_api_key
ENCRYPTION_KEY={encryption_key}
"""
        
        if 'REDIS_HOST' not in content:
            content = content.replace('"""', additions + '"""')
        
        with open('quick_setup.py', 'w') as f:
            f.write(content)
        print("✅ Đã cập nhật quick_setup.py")

if __name__ == "__main__":
    print("🔧 Sửa lỗi cấu hình Suna...")
    update_env_files()
    print("✅ Hoàn tất!")