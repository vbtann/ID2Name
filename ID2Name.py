import csv
import argparse
import sys

def main():
    # Khởi tạo xử lý tham số dòng lệnh trong commandline
    parser = argparse.ArgumentParser(description='Chuyển đổi MSSV thành Họ tên')
    parser.add_argument('data_file', help='Đường dẫn đến file chứa dữ liệu sinh viên')
    parser.add_argument('input_file', help='Đường dẫn đến file cần chuyển đổi')
    parser.add_argument('output_file', help='Đường dẫn đến file chứa kết quả chuyển đổi')
    
    # Xử lý tham số dòng lệnh
    args = parser.parse_args()
    
    try:
        # Đọc thông tin sinh viên từ file dữ liệu vào mảng student_dict
        student_dict = {}
        with open(args.data_file, mode="r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Bỏ qua Header của file csv
            for row in csv_reader:
                if len(row) >= 2:
                    student_dict[int(row[0])] = row[1]
        
        # Thông báo đã khởi tạo mảng dữ liệu
        print(f"Đã hoàn tất tải {len(student_dict)} dữ liệu sinh viên từ {args.data_file}")
        
        # Xử lý MSSV và ghi đầu ra
        records_processed = 0
        records_found = 0
        
        with open(args.input_file, mode="r", encoding="utf-8") as inf, \
             open(args.output_file, mode="w", newline="", encoding="utf-8") as outf:
            
            csv_reader = csv.reader(inf)
            next(csv_reader, None)  # Bỏ qua Header của file csv
            
            writer = csv.writer(outf)
            writer.writerow(["MSSV", "Họ tên"])
            
            for row in csv_reader:
                try:
                    if row:
                        student_id = int(row[0])
                        records_processed += 1
                        
                        name = student_dict.get(student_id, "Không tìm thấy thông tin")
                        if name != "Không tìm thấy thông tin":
                            records_found += 1
                            
                        writer.writerow([student_id, name])
                except ValueError:
                    print(f"Cảnh báo: Không thể xử lý dòng: {row}")
                    continue
        
        # Thông báo kết quả
        print(f"Đã xử lý {records_processed} MSSV, tìm thấy {records_found} kết quả")
        print(f"Kết quả đã được lưu vào {args.output_file}")
        
    except FileNotFoundError as e:
        print(f"Lỗi: Không tìm thấy file - {e.filename}")
        sys.exit(1)
    except PermissionError:
        print(f"Lỗi: Không thể truy cập vào một trong các file")
        sys.exit(2)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(3)

if __name__ == "__main__":
    main()