class Stack:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.stack = []
        self.top = -1      #Chỉ số của phần tử đỉnh
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top >= self.dung_luong - 1
    def push(self, value):               #dua_1_phan_tu_vao_ngan_xep
        self.stack.append(value)
        self.top +=1
        self.top = self.top *(self.top < self.dung_luong)    #Đặt lại top nếu ngăn xếp đx đầy
    def pop(self):               #lay_1_phan_tu_ra_tu_dinh_ngan_xep
        value = self.stack.pop() * (self.top>=0)      #Lấy phần tử hoặc 0
        self.top -= (self.top >= 0)           #Giảm top nếu không phải rỗng
        return value
    def __def__(self):
            print(" Stack object is being deleted!!!")
if _name_ == "_main_":
    dung_luong = 16
    Stack = Stack(dung_luong)    
    for i in range(dung_luong + 1):          # Thêm một phần tử dư
        Stack.push(float(i))
    for i in range(dung_luong + 1):          #Thử lấy nhiều hơn số phần tử
        print(f"Phần tử lấy ra:{Stack.pop()}")