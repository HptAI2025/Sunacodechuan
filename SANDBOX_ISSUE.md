# 🚨 SANDBOX PROXY ISSUE

## Vấn đề hiện tại

Có vấn đề với proxy mapping của sandbox environment:
- Frontend đang chạy tốt trên localhost:12001 (production build)
- Backend đang chạy tốt trên localhost:12000
- Tuy nhiên external URLs không thể truy cập được do vấn đề proxy

## Trạng thái services

✅ **Backend API**: http://localhost:12000 - Hoạt động bình thường
✅ **Frontend**: http://localhost:12001 - Production build hoạt động bình thường
❌ **External URLs**: Không thể truy cập do vấn đề proxy mapping

## Giải pháp tạm thời

Người dùng có thể:
1. Clone repository về máy local
2. Chạy `npm install` trong thư mục frontend
3. Chạy `npm run dev` để start development server
4. Truy cập http://localhost:3000

## Các thử nghiệm đã thực hiện

1. ✅ Restart frontend với port 12001
2. ✅ Restart frontend với port 3000  
3. ✅ Build production và serve với npm start
4. ✅ Thử simple HTTP server
5. ❌ Tất cả đều không giải quyết được vấn đề proxy mapping

## Kết luận

Vấn đề nằm ở cấu hình proxy của sandbox environment, không phải ở code của Suna.
Suna hoạt động hoàn toàn bình thường khi chạy local.