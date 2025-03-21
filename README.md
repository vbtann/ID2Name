# Công cụ chuyển đổi MSSV sang Họ tên

## Hướng dẫn tải
```bash
git clone https://github.com/vbtann/ID2Name.git
cd ID2Name
```

## Cú pháp sử dụng
```
python3 Id2Name.py data.csv input.csv output.csv
```

Trong đó: \
    **data.csv** : Đường dẫn đến file data đã có trên github \
    **input.csv** : Đường dẫn đến file MSSV cần chuyển đổi \
    **output.csv** : Đường dẫn đến file đầu ra gồm thông tin đã chuyển đổi
    
Ví dụ: 
`python3 Id2Name.py data.csv example_input.csv example_output.csv`

## Định dạng dữ liệu
`File dữ liệu`: Một file **csv**, gồm thông tin mỗi sinh viên như sau:
>StudentID,Name,Email,Khoa,Ngành,Chương trình\
>21110001,LÊ TRẦN DUY ANH,21110001@student.hcmus.edu.vn,Toán - Tin học,"Nhóm ngành Toán học, Toán tin, Toán ứng dụng",Chuẩn

`File đầu vào`: Một file **csv**, gồm mỗi MSSV một dòng

`File kết quả`: Một file **csv**, với định dạng như sau:
>MSSV,Họ tên\
>21111111,Nguyễn Văn B