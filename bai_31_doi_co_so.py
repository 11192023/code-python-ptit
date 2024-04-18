def convert_base(n, base):
    if n == 0:
        return '0'
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    while n > 0:
        result = digits[n % base] + result
        n //= base
    
    return result

# Đọc số lượng bộ test
num_tests = int(input())

# Vòng lặp để xử lý từng bộ test
for _ in range(num_tests):
    # Nhập số nguyên dương N và cơ số b
    N, b = map(int, input().split())
    
    # Chuyển đổi và in kết quả
    print(convert_base(N, b))
