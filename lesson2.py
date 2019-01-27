'''
基础
列表
标志
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
'''
list1 = ['a','b','1']

#基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
list1 = ['a','b','c',1]
list1.append('d')#在末尾增加元素
list1.pop()#删除末尾元素
#del是python语句，而不是列表方法，无法通过list来调用。使用del可以删除一个元素，当元素删除之后，位于它后面的元素会自动移动填补空出来的位置。
del list1[2]
#使用列表内置的copy方法，是将新列表中的元素指向了与原列表相同的内存空间。但是，如果列表中嵌套了列表，拷贝后的列表中嵌套的列表元素指针，指向原列表中嵌套列表的整体地址，而不是指向嵌套列表中元素的内存地址。
s = [[1,2],3,4]
s1 = s.copy()
s1[1] = 'oliver'
s1[0][1] = 'hello'
print('列表s：',s)
print('列表s1:',s1)
import  copy
s2 = copy.deepcopy(s)
s2[0][1] = 'abc'
print('列表s：',s)
print('列表s2：',s2)
#使用copy.deepcopy（）方法来拷贝列表，修改嵌套列表中的元素，原列表不受影响。
#1、浅拷贝只能拷贝最外层，修改内层则原列表和新列表都会变化。
#2、深拷贝是指将原列表完全克隆一份新的。

#列表相关方法
'''
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表
Python包含以下方法:

1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
'''

#元组Python 的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Python', 'js', 1989, 1644);
#访问元组
tup1[0]
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup2 = ('aa','bb','cc','dd')
tup3 = tup1 + tup2
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
#元组运算符与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
#元组内置函数
#len(tup1)
#max(tup1)
#min(tup1)

#元组和列表转换
tup4 = tuple(list1)
list4 = list(tup4)

#作页
family_list = [{'father':''},{'mother':''},{'wife':''}]
family_list[0]['father'] = 'cc'#增加名字
family_list[1]['mother'] = 'jj'#增加名字
family_list[2]['wife'] = 'll'#增加名字
family_list[0]['father'] = ''#删除名字
family_list[1]['mother'] = ''#删除名字
family_list[2]['wife'] = ''#删除名字

