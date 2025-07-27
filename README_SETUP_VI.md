# 🚀 Hướng dẫn cài đặt Suna nhanh

## 📋 Yêu cầu hệ thống

- Python 3.11+
- Node.js 18+
- Git
- Redis (sẽ được cài tự động)

## ⚡ Cài đặt nhanh (Recommended)

### Bước 1: Clone repository
```bash
git clone https://github.com/kortix-ai/suna.git
cd suna
```

### Bước 2: Chạy script cài đặt tự động
```bash
python quick_setup.py
```

### Bước 3: Khởi chạy tất cả services
```bash
python start_services.py
```

### Bước 4: Truy cập ứng dụng
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## 🔧 Cài đặt thủ công

### 1. Tạo file cấu hình
```bash
# Copy template và điền thông tin
cp .env.template .env
cp frontend/.env.local.template frontend/.env.local

# Chỉnh sửa file .env với API keys của bạn
nano .env
nano frontend/.env.local
```

### 2. Cài đặt dependencies

#### Backend:
```bash
cd backend
pip install uv
uv sync
cd ..
```

#### Frontend:
```bash
cd frontend
npm install
cd ..
```

### 3. Cài đặt Redis
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install redis-server

# macOS
brew install redis

# Khởi chạy Redis
redis-server --daemonize yes
```

### 4. Khởi chạy services

#### Terminal 1 - Backend:
```bash
cd backend
uv run uvicorn api:app --host 0.0.0.0 --port 8000
```

#### Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

## 🔑 API Keys cần thiết

### Bắt buộc:
- **Supabase**: Database và authentication
  - Tạo tại: https://supabase.com/
  - Cần: URL, ANON_KEY, SERVICE_ROLE_KEY

### Khuyến nghị:
- **Morph LLM**: AI code editing
  - Tạo tại: https://morphllm.com/api-keys
- **Tavily**: Web search
  - Tạo tại: https://tavily.com/
- **Firecrawl**: Web scraping
  - Tạo tại: https://www.firecrawl.dev/

### Tùy chọn:
- **Daytona**: Cloud development environments
- **QStash**: Background job processing
- **Ngrok**: Tunneling service

## 🛠️ Scripts tiện ích

### `quick_setup.py`
Cài đặt tự động với API keys có sẵn

### `start_services.py`
Khởi chạy tất cả services trong background

### `auto_setup.py`
Cài đặt dependencies và cấu hình cơ bản

## 📁 Cấu trúc project

```
suna/
├── backend/              # FastAPI backend
├── frontend/             # Next.js frontend
├── docs/                 # Documentation
├── .env.template         # Environment template
├── quick_setup.py        # Quick setup script
├── start_services.py     # Service launcher
└── README_SETUP_VI.md    # This file
```

## 🐛 Troubleshooting

### Lỗi port đã được sử dụng:
```bash
# Tìm và kill process
lsof -ti:8000 | xargs kill -9
lsof -ti:3000 | xargs kill -9
```

### Lỗi Redis connection:
```bash
# Kiểm tra Redis
redis-cli ping

# Khởi chạy lại Redis
redis-server --daemonize yes
```

### Lỗi dependencies:
```bash
# Backend
cd backend && uv sync --reinstall

# Frontend
cd frontend && rm -rf node_modules && npm install
```

## 📞 Hỗ trợ

- GitHub Issues: https://github.com/kortix-ai/suna/issues
- Documentation: https://docs.suna.ai
- Discord: https://discord.gg/suna

## 🎯 Bước tiếp theo

1. Đọc documentation để hiểu các tính năng
2. Cấu hình thêm AI providers (OpenAI, Anthropic, etc.)
3. Thiết lập production deployment
4. Tùy chỉnh UI/UX theo nhu cầu