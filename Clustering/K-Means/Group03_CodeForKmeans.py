#. Import thư viện và tải dữ liệu**
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Đường dẫn tệp CSV
file_path = 'D:/ThanhMy/DUE_HK5/kho_khai_pha_du_lieu_phanDinhVan/cuoi_ky/nop/Mall_Customers.csv'
print(os.path.exists(file_path))  # Kiểm tra xem tệp có tồn tại không

# Đọc dữ liệu từ file CSV vào biến data
data = pd.read_csv(file_path)

# Hiển thị thông tin ban đầu của dữ liệu
print(data.head())
print(data.info())


# Chuyển đổi giới tính thành số
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Xóa cột không cần thiết nếu có (vd: CustomerID)
data = data.drop(columns=['CustomerID'])

# Kiểm tra giá trị bị thiếu
print(data.isnull().sum())

# Chuẩn hóa dữ liệu**
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])

# Hiển thị dữ liệu đã chuẩn hóa
print(pd.DataFrame(data_scaled, columns=['Age', 'Annual Income (k$)', 'Spending Score (1-100)']).head())



# Tìm số cụm tối ưu bằng Elbow Method**
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Vẽ biểu đồ Elbow
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Optimal k')
plt.show()

# Áp dụng K-Means Clustering**
#Dựa trên số cụm k tối ưu (giả sử k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(data_scaled)

# Thêm cột Cluster vào dữ liệu ban đầu
data['Cluster'] = clusters
print(data.head())

# Trực quan hóa các cụm**
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=data['Annual Income (k$)'],
    y=data['Spending Score (1-100)'],
    hue=data['Cluster'],
    palette='viridis',
    s=100
)
plt.title('Customer Segmentation')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(title='Cluster')
plt.show()

# **8. Phân tích cụm**
cluster_summary = data.groupby('Cluster').mean()
print(cluster_summary)
