# Big data with Neo4j

## Graph-Based Recommendations

Tạo các đề xuất được cá nhân hóa là một trong những trường hợp sử dụng phổ biến nhất đối với cơ sở dữ liệu biểu đồ. Một số lợi ích chính của việc sử dụng biểu đồ để tạo các đề xuất bao gồm:
-	Hiệu suất. Không index cho phép tính toán các đề xuất trong thời gian thực, đảm bảo đề xuất luôn có liên quan và phản ánh thông tin cập nhật.

-	Data model. Mô hình biểu đồ thuộc tính được gắn nhãn cho phép dễ dàng kết hợp các bộ dữ liệu từ nhiều nguồn, cho phép các doanh nghiệp mở khóa giá trị từ các kho dữ liệu đã tách biệt trước đó

## How to start project

- Trước khi run ứng dụng, cần tải sẵn một số thư viện sau: 

```py
!pip install neo4j #driver
!pip install FastAPI
!pip install uvicorn
```

- Xong khi hoàn tất cài đặt, tiến hành khởi động ứng dụng bằng command line: 

```
uvicorn project_app:app
```

Kết quả thu được như sau: 

```
INFO:     Started server process [11124]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```