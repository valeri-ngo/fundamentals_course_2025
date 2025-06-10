number = int(input())
rows = int(input())
#
# for i in range(1 , number +1):       ## Right-Angled
#     for k in range (0 , i ):
#         print('*' , end='')
#     print()
#
# for i in range(number):        ## Square with Hollow Center
#     if i == 0 or i == number -1:
#         print('*' * number)
#     else:
#         print('*' + ' ' * (number - 2) + '*')
#
for i in range(number):
    if i