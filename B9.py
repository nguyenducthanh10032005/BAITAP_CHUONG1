import math

class DaGiac:
    def __init__(self, so_canh, do_dai_canh):
        self.so_canh = so_canh
        self.do_dai_canh = do_dai_canh

    def tinh_chu_vi(self):
        return self.so_canh * self.do_dai_canh

    def tinh_dien_tich(self):
        raise NotImplementedError("Phương thức này cần được cài đặt trong lớp con.")

class HinhBinhHanh(DaGiac):
    def __init__(self, do_dai, do_rong):
        super().__init__(4, do_dai)  # Hình bình hành có 4 cạnh
        self.do_dai = do_dai
        self.do_rong = do_rong

    def tinh_chu_vi(self):
        return 2 * (self.do_dai + self.do_rong)

    def tinh_dien_tich(self):
        return self.do_dai * self.do_rong

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, do_dai, do_rong):
        super().__init__(do_dai, do_rong)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

if __name__ == "__main__":
    # Nhập thuộc tính cho Hình Vuông
    canh = float(input("Nhập cạnh của hình vuông: "))
    hinh_vuong = HinhVuong(canh)
    print(f"Chu vi hình vuông: {hinh_vuong.tinh_chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.tinh_dien_tich()}")

    # Nhập thuộc tính cho Hình Chữ Nhật
    do_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    do_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    hinh_chu_nhat = HinhChuNhat(do_dai, do_rong)
    print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.tinh_chu_vi()}")
    print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.tinh_dien_tich()}")

    # Nhập thuộc tính cho Hình Bình Hành
    do_dai_binh_hanh = float(input("Nhập chiều dài của hình bình hành: "))
    do_rong_binh_hanh = float(input("Nhập chiều rộng của hình bình hành: "))
    hinh_binh_hanh = HinhBinhHanh(do_dai_binh_hanh, do_rong_binh_hanh)
    print(f"Chu vi hình bình hành: {hinh_binh_hanh.tinh_chu_vi()}")
    print(f"Diện tích hình bình hành: {hinh_binh_hanh.tinh_dien_tich()}")


