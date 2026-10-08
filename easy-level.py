# def sum_range(start, end):
#     if start > end:
#         end, start = start, end
#     return sum(range(start, end + 1))
# print(sum_range(2, 12))
# print(sum_range(-4, 4))
# print(sum_range(3, 2))

# n = 1
# sum = 0
# while n!=0:
#     n = int(input())
#     if n >= 100 and n <= 999 and n % 4 == 0:
#         sum = sum + n
# print(sum)

# n = int(input())
# min = 99999999999999
# e = 0
# for i in range(n):
#     a = int(input())
#     e = a % 10
#     if e == 6:
#         if a < min:
#             min = a
# print(min)