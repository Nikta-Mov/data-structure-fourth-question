class DoubleEndedQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0
    
    def push_back(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def push_front(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.first = (self.first - 1) % self.max_size
        self.Q[self.first] = item
        self.num += 1

    def pop_front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

# پیش‌فرض‌ها: توابعی که برای ویژگی‌های برنامه نیاز دارند در اینجا یا قبل از این بخش تعریف شده‌اند

polynomials = []  # لیستی برای نگهداری چند جمله‌ای‌ها

# تکمیل بخش ورودی کاربر
while True:
    user_input = input("1 را برای وارد کردن، 2 را برای حذف کردن، 3 را برای چاپ، 4 را برای جمع، 5 را برای ضرب دو چندجمله‌ای و 6 را برای خروج وارد کنید: ")
    
    if user_input == '1':
        get_and_store_polynomial()
        print("چند جمله‌ای ذخیره شد:", polynomials)
    elif user_input == '2':
        if polynomials:
            remove_polynomial()
        else:
            print("هیچ چند جمله‌ای‌ای برای حذف وجود ندارد.")
    elif user_input == '3':
        if polynomials:
            print_polynomial()
        else:
            print("هیچ چند جمله‌ای‌ای برای چاپ کردن وجود ندارد.")
    elif user_input == '4':
        if len(polynomials) > 1:
            add_and_simplify_polynomials()
        else:
            print("حداقل نیاز به دو چند جمله‌ای برای جمع کردن است.")
    elif user_input == '5':
        if len(polynomials) > 1:
            multiply_and_simplify_polynomials()
        else:
            print("حداقل نیاز به دو چند جمله‌ای برای ضرب کردن است.")
    elif user_input == '6':
        print("با تشکر از استفاده شما، برنامه خاتمه یافت.")
        break
    else:
        print("ورودی نامعتبر است. لطفاً یک عدد صحیح از 1 تا 6 وارد کنید.")