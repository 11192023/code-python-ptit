from math import sqrt

# class point 
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

# class triangle
class Triangle: 
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def distance(self, p1, p2):
        return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def is_valid_triangle(self):
        a = self.distance(self.point_a, self.point_b)
        b = self.distance(self.point_b, self.point_c)
        c = self.distance(self.point_c, self.point_a)

        # Kiểm tra điều kiện tam giác
        if a + b > c and b + c > a and c + a > b:
            return round(a + b + c, 3)
        else:
            return "INVALID"

# Main function
if __name__ == "__main__":
    # Số bộ test case
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        # Nhập tọa độ 3 điểm
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        point_a = Point(x1, y1)
        point_b = Point(x2, y2)
        point_c = Point(x3, y3)

        # Tạo tam giác và kiểm tra
        triangle = Triangle(point_a, point_b, point_c)
        print(triangle.is_valid_triangle())
