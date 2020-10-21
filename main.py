#無窮迴圈
'''
num = 0
while True:
  print('num = {}'.format(num))
  num += 1
'''

'''
for i in range(10):
 if i == 8 :
  break #終止
  print(i)
'''

'''
for i in range(10):
 if i == 8 :
  continue #換到下一個迴圈
  print(i)
'''

'''
x = int(input())

y = x if x > 10 else 10

print('y 的值為 {}'.format(y))
'''

'''
x = int(input())
if x > 10:
		y = x
else:
		y = 10
print('y 的值為 {}'.format(y))
'''

'''
number = [34 , 58 , 95 , 81]

list1 = ['Rex', 20 , 180.2 ]

list2 = [[1 , 2],[3 , 4]]
print(list2)
'''

'''
li = [1 ,2 ,3 ,4]
li = list()

print(li)
print(* li)
'''

'''
numbers = [1, 2, 3, 4]
print(numbers[0:4:2]) #實質0到3 跳2格
'''

'''
li = [38, 85]
numbers = [1, 2, 3, 4]
numbers.append(38)  #新增值(只能一個))
numbers.extend(li)  #新增值
numbers.insert(2, 34)  #第三個位置被換成了34，舊的第三位被移到後面了\
numbers[2] = 8          #把位置三的數替換成8
print(numbers)
numbers.pop()      #刪掉某位置的數
print(numbers)
numbers.remove(38) #刪除某個元素
print(numbers)
'''

'''
nums = [5, 2, 1, 5, 7, 8, 9]
nums.reverse()   #翻轉
nums.sort()     #小到大
nums.sort(reverse = True) #大到小
print(nums)
'''

'''
nums = [5, 2, 1, 5, 7, 8, 9]
for i in nums:
  print(i)
len(nums) #長度
max(nums) #最大值
max(nums) #最小值
'''
'''
li = ('資工', '養殖', '商船', '海洋')
print(type(li))
tp = tuple(li)
'''

'''
dic = {'name': 'Rex', 'age': 20, 'student?':True}
print(dic.pop('name')) #刪除同時回傳
print(dic)
del dic['age']
print(dic)
#dic.clear('student?')
print(dic)
'''

'''
dic = {'name': 'Rex'}
dic.update({'age': 20}) #新增資訊
'''


dic = {'name': 'Rex', 'age': 20, 'student?':True}
print(dic.keys()) #性質
print(dic.values()) #內容