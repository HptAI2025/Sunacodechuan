# 🚀 Hướng dẫn cài đặt Suna - Tiếng Việt

## 📖 Giới thiệu

Suna là một AI agent mã nguồn mở có khả năng:
- Tạo và chỉnh sửa code
- Tìm kiếm thông tin trên web
- Tương tác với các API và services
- Tự động hóa các tác vụ phát triển

## 🎯 Cài đặt nhanh (1 phút)

```bash
# 1. Clone repository
git clone https://github.com/kortix-ai/suna.git
cd suna

# 2. Chạy script cài đặt tự động
python quick_setup.py

# 3. Khởi chạy tất cả services
python start_services.py

# 4. Truy cập http://localhost:3000
```

## 📋 Yêu cầu hệ thống

- **Python 3.11+**
- **Node.js 18+** 
- **Git**
- **Redis** (sẽ được cài tự động)

## 🔧 Cài đặt chi tiết

### Bước 1: Chuẩn bị môi trường

```bash
# Kiểm tra Python
python3 --version  # Cần >= 3.11

# Kiểm tra Node.js
node --version     # Cần >= 18

# Cài đặt UV (Python package manager)
pip install uv
```

### Bước 2: Clone và setup

```bash
git clone https://github.com/kortix-ai/suna.git
cd suna

# Kiểm tra setup hiện tại
python test_setup.py
```

### Bước 3: Cấu hình API Keys

```bash
# Tạo file cấu hình từ template
cp .env.example .env
cp frontend/.env.example frontend/.env.local

# Chỉnh sửa file .env
nano .env
```

#### API Keys cần thiết:

**🔴 Bắt buộc:**
- **Supabase** (Database): https://supabase.com/
  ```
  SUPABASE_URL=https://your-project.supabase.co
  SUPABASE_ANON_KEY=your_anon_key
  SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
  ```

**🟡 Khuyến nghị:**
- **Morph LLM** (AI Code): https://morphllm.com/api-keys
  ```
  MORPH_API_KEY=your_morph_key
  ```
- **Tavily** (Web Search): https://tavily.com/
  ```
  TAVILY_API_KEY=your_tavily_key
  ```

**🟢 Tùy chọn:**
- **Anthropic/OpenAI** (LLM): https://console.anthropic.com/
- **Firecrawl** (Web Scraping): https://www.firecrawl.dev/
- **QStash** (Background Jobs): https://console.upstash.com/

### Bước 4: Cài đặt dependencies

```bash
# Backend
cd backend
uv sync
cd ..

# Frontend  
cd frontend
npm install
cd ..
```

### Bước 5: Khởi chạy services

#### Tự động (Khuyến nghị):
```bash
python start_services.py
```

#### Thủ công:
```bash
# Terminal 1 - Redis
redis-server

# Terminal 2 - Backend
cd backend
uv run uvicorn api:app --host 0.0.0.0 --port 8000

# Terminal 3 - Frontend
cd frontend
npm run dev
```

## 🌐 Truy cập ứng dụng

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🛠️ Scripts tiện ích

| Script | Mô tả |
|--------|-------|
| `quick_setup.py` | Cài đặt tự động với API keys có sẵn |
| `start_services.py` | Khởi chạy tất cả services |
| `test_setup.py` | Kiểm tra cài đặt |
| `auto_setup.py` | Cài đặt dependencies cơ bản |

## 🐛 Troubleshooting

### Lỗi thường gặp:

**Port đã được sử dụng:**
```bash
# Kill processes trên port
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

**Redis không kết nối được:**
```bash
# Kiểm tra Redis
redis-cli ping

# Khởi chạy Redis
redis-server --daemonize yes
```

**Dependencies lỗi:**
```bash
# Reinstall backend
cd backend && uv sync --reinstall

# Reinstall frontend
cd frontend && rm -rf node_modules && npm install
```

**Supabase connection error:**
- Kiểm tra URL và API keys trong `.env`
- Đảm bảo Supabase project đã được tạo
- Kiểm tra network connection

## 📁 Cấu trúc project

```
suna/
├── backend/                 # FastAPI backend
│   ├── api.py              # Main API
│   ├── pyproject.toml      # Dependencies
│   └── ...
├── frontend/               # Next.js frontend
│   ├── pages/              # React pages
│   ├── components/         # UI components
│   ├── package.json        # Dependencies
│   └── ...
├── docs/                   # Documentation
├── .env.example           # Environment template
├── quick_setup.py         # Quick setup script
├── start_services.py      # Service launcher
├── test_setup.py          # Setup checker
└── README.md              # Main documentation
```

## 🔒 Bảo mật

- ✅ File `.env` đã được thêm vào `.gitignore`
- ✅ API keys không được commit lên Git
- ✅ Sử dụng template files cho cấu hình
- ⚠️ Không share API keys trong public repositories

## 🚀 Production Deployment

### Docker (Khuyến nghị):
```bash
# Build và chạy với Docker Compose
docker-compose up -d
```

### Manual:
```bash
# Build frontend
cd frontend && npm run build

# Start production servers
cd backend && uv run uvicorn api:app --host 0.0.0.0 --port 8000
cd frontend && npm start
```

## 📞 Hỗ trợ

- **GitHub Issues**: https://github.com/kortix-ai/suna/issues
- **Documentation**: https://docs.suna.ai
- **Discord**: https://discord.gg/suna
- **Email**: support@suna.ai

## 🎯 Bước tiếp theo

1. **Khám phá tính năng**: Thử tạo code với AI
2. **Cấu hình nâng cao**: Thêm LLM providers
3. **Tùy chỉnh**: Chỉnh sửa UI/UX
4. **Deploy**: Đưa lên production
5. **Đóng góp**: Tham gia phát triển

## 📄 License

MIT License - Xem file `LICENSE` để biết thêm chi tiết.

---

**🌟 Nếu Suna hữu ích, hãy star repository này!**