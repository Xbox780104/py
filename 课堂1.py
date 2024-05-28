# lst=[]
# for i in range(10):
#     lst.append(i)
# print(lst)

# lst1 = [i for i in range(10)]
# print(lst1)

# ls=[i^2+3 for i in range(10)]
# print(ls)

# lst2D=[[1,1,1,1,2,4,3,4,8]]
# print(len(lst2D)) 

# s5={x**y for x in range(10) if x%2==1 for y in range(1,5)}
# print(s5)

# file_name=r'C:\Users\HP\Desktop\问题集.txt'
# fp=open(file=file_name,mode='r',encoding='utf-8')
# rows=fp.readlines()
# for row in rows:
#     print(row,end='')
# fp.close()
# fp=None
#with 方法可以保证文件关闭

# file_name=r"C:\Users\HP\Desktop\1.txt"
# with open(file=file_name,mode='r',encoding='utf-8') as fp:
#     rows=fp.readlines()
#     for row in rows:
#         print(row,end='')

# def my_power() -> None:
#     pass

# def charge(name:str,age:int):
#     if age<18:
#         word='{}是青少年'.format(name) 
#     elif age>18 and age<=40:
#         word='{}是壮年'.format(name)
#     elif age>40 and age<60:
#         word='{}是中年'.format(name)
#     else:
#         word='{}是老年'.format(name)
#     return word
    
# # p=charge('lmx',23)
# # print(p)

# if __name__=='__main__':
#     my_name=eval(input())
#     my_age=eval(input())
#     rst=charge(my_name,my_age)
#     print(rst)



# def bmji(*,year,*items,**t):

#     return [(),(),()]

# def findItem(ItemN,BMList):
#     return ((ItemN,1,10),(ItemN,2,0))