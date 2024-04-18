# Hàm tính tổng số tiền và phụ phí dựa trên chỉ số cũ và mới
def calculate_bill(old_reading, new_reading):
    # Tính số m3 tiêu thụ
    consumption = new_reading - old_reading
    
    # Tính tổng số tiền nước tiêu thụ
    if consumption <= 50:
        unit_price = 100
        additional_fee = 0.02
    elif consumption <= 100:
        unit_price = 150
        additional_fee = 0.03
    else:
        unit_price = 200
        additional_fee = 0.05
    
    water_bill = consumption * unit_price
    additional_charge = water_bill * additional_fee
    
    total_bill = water_bill + additional_charge
    return total_bill

# Nhập số lượng khách hàng
num_customers = int(input())

# Danh sách khách hàng và thông tin hóa đơn
customer_bills = []

# Nhập thông tin khách hàng và tính toán hóa đơn cho từng khách hàng
for i in range(num_customers):
    customer_name = input()
    new_reading = int(input())  # Chỉ số mới
    old_reading = int(input())  # Chỉ số cũ
    
    total_bill = calculate_bill(old_reading, new_reading)
    customer_bills.append((customer_name, total_bill))

# Sắp xếp danh sách khách hàng theo tổng số tiền giảm dần
customer_bills.sort(key=lambda x: x[1], reverse=True)

# In ra danh sách khách hàng đã sắp xếp
for i, (customer_name, total_bill) in enumerate(customer_bills, start=1):
    print(f"KH{i:02d} {customer_name} {round(total_bill)}")
