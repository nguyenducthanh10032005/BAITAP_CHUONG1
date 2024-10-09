class Hinh_Chu_Nhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def chu_vi_hcn(self):
        return 2 * (self.length + self.width)

    def dien_tich_hcn(self):
        return self.length * self.width
#Tạo 1 lớp đối tượng mới từ lớp HCN
Hinh_Chu_Nhat = Hinh_Chu_Nhat(6, 3) 

#Gọi phương thức diện tích hình chữ nhật để tính diện tích hcn và gán kết quả cho biến
dientich = Hinh_Chu_Nhat.dien_tich_hcn()  
chuvi = Hinh_Chu_Nhat.chu_vi_hcn() 

print(f"Độ dài cạnh dài: ", Hinh_Chu_Nhat.length)
print(f"Độ dài cạnh ngắn: ", Hinh_Chu_Nhat.width)
print(f"Chu vi hình chữ nhật:", chuvi)
print(f"Diện tích hình chữ nhật:", dientich)



