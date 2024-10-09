class Ngay:
    def __init__(self, day=7, month=10, year=2024):
        self.day=day
        self.month=month
        self.year=year
    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")
    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day +=1
if __name__ == "_main_":
    date = Ngay(8, 10, 2024)
    print("Ngày  hiện tại: ")
    date.display()
    date.next()
    print("Ngày tiếp theo:")
    date.display()