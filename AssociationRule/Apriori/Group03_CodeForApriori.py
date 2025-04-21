import pandas as pd

# Đường dẫn file gốc
file_path = r"D:\data\spa_customer_association_rules.csv"

# Đọc dữ liệu từ file CSV với dấu phân cách là dấu chấm phẩy
df = pd.read_csv(file_path, sep=';')

# Danh sách các cột cần chuyển đổi
columns_to_convert = [
    "Membership", "Regular Visits", "Purchased Package", "Uses Discounts",
    "Referred Friends", "Takes Survey", "Attends Events", "Feedback Provided"
]

# Chuyển đổi giá trị "Yes/No" thành 1/0
for col in columns_to_convert:
    if col in df.columns:  # Kiểm tra nếu cột tồn tại trong dữ liệu
        df[col] = df[col].replace({"Yes": 1, "No": 0})

# Kiểm tra kết quả sau khi chuyển đổi
print("Dữ liệu sau khi chuyển đổi:")
print(df.head())

# Lưu dữ liệu đã chuyển đổi vào file mới, sử dụng dấu phân cách là dấu chấm phẩy
updated_file_path = r"D:\data\spa_customer_association_rules_binary.csv"
df.to_csv(updated_file_path, sep=';', index=False)

print("\nHoàn thành chuyển đổi. File đã lưu tại:", updated_file_path)
