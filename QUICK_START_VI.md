# 🚀 HƯỚNG DẪN CHẠY SUNA NHANH

## 📋 YÊU CẦU HỆ THỐNG

- **Python 3.12+** 
- **Node.js 18+** và npm
- **Redis** server
- **Git**

## ⚡ CÁCH 1: CÀI ĐẶT TỰ ĐỘNG (KHUYẾN NGHỊ)

### 1. Clone repository
```bash
git clone https://github.com/kortix-ai/suna.git
cd suna
```

### 2. Chạy script cài đặt tự động
```bash
python quick_setup.py
```

Script sẽ tự động:
- ✅ Kiểm tra yêu cầu hệ thống
- ✅ Cài đặt uv (Python package manager)
- ✅ Cài đặt Redis nếu chưa có
- ✅ Cài đặt backend dependencies (151 packages)
- ✅ Cài đặt frontend dependencies (935 packages)
- ✅ Tạo file cấu hình .env với API keys
- ✅ Test kết nối database và Redis

### 3. Khởi chạy tất cả services
```bash
python start_services.py
```

### 4. Truy cập ứng dụng
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🔧 CÁCH 2: CÀI ĐẶT THỦ CÔNG

### 1. Cài đặt dependencies hệ thống

**macOS:**
```bash
brew install python@3.12 node redis
brew services start redis
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.12 python3.12-pip nodejs npm redis-server
sudo systemctl start redis-server
```

**Windows:**
```bash
# Cài đặt Python 3.12 từ python.org
# Cài đặt Node.js từ nodejs.org
# Cài đặt Redis từ https://redis.io/download
```

### 2. Cài đặt uv (Python package manager)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Hoặc trên Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Clone và setup project
```bash
git clone https://github.com/kortix-ai/suna.git
cd suna
```

### 4. Cài đặt backend
```bash
cd backend
uv sync
cd ..
```

### 5. Cài đặt frontend
```bash
cd frontend
npm install
cd ..
```

### 6. Tạo file cấu hình
```bash
cp .env.example .env
cp frontend/.env.example frontend/.env.local
```

### 7. Cập nhật API keys trong file .env
```bash
# Mở file .env và điền các API keys:
# - SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY
# - MORPH_API_KEY (cho LLM)
# - TAVILY_API_KEY (cho web search)
# - FIRECRAWL_API_KEY (cho web scraping)
# - Các keys khác theo nhu cầu
```

### 8. Khởi chạy services

**Terminal 1 - Redis:**
```bash
redis-server
```

**Terminal 2 - Backend:**
```bash
cd backend
uv run uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 3 - Frontend:**
```bash
cd frontend
npm run dev
```

## 🔑 LẤY API KEYS

### Supabase (Database)
1. Truy cập https://supabase.com
2. Tạo project mới
3. Vào Settings > API
4. Copy URL, anon key, service_role key

### Morph (LLM)
1. Truy cập https://morph.so
2. Đăng ký tài khoản
3. Tạo API key

### Tavily (Web Search)
1. Truy cập https://tavily.com
2. Đăng ký tài khoản
3. Tạo API key

### Firecrawl (Web Scraping)
1. Truy cập https://firecrawl.dev
2. Đăng ký tài khoản
3. Tạo API key

## 🛠️ TROUBLESHOOTING

### Lỗi Redis connection
```bash
# Kiểm tra Redis đang chạy
redis-cli ping
# Nếu không có response, khởi chạy Redis:
redis-server
```

### Lỗi Python dependencies
```bash
# Cài đặt lại dependencies
cd backend
uv sync --reinstall
```

### Lỗi Node.js dependencies
```bash
# Xóa node_modules và cài đặt lại
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Lỗi port đã được sử dụng
```bash
# Tìm và kill process đang dùng port
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
```

## 📱 SỬ DỤNG SUNA

1. **Truy cập**: http://localhost:3000
2. **Đăng nhập**: Tạo tài khoản hoặc đăng nhập
3. **Tạo Agent**: Click "New Agent" để tạo AI agent
4. **Chat**: Bắt đầu chat với agent của bạn
5. **Tools**: Agent có thể sử dụng web search, code execution, file operations

## 🔒 BẢO MẬT

- ❌ **KHÔNG** commit file `.env` lên Git
- ✅ Sử dụng `.env.example` làm template
- ✅ API keys được mã hóa trong database
- ✅ Sử dụng HTTPS trong production

## 📞 HỖ TRỢ

Nếu gặp vấn đề:
1. Kiểm tra file `TEST_REPORT_VI.md` để xem các lỗi đã biết
2. Chạy `python test_setup.py` để kiểm tra hệ thống
3. Xem logs trong terminal để debug
4. Tạo issue trên GitHub repository

---

**🎉 Chúc bạn sử dụng Suna vui vẻ!**