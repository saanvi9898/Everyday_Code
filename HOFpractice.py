def add(a,b): return a+b
def sub(a,b): return a-b
opt={'sum':add, 'diff':sub}
print(opt['sum'](10,5))
print(opt['diff'](10,5))
# builtin HOF

#map()
# print odd even on list 1 to 5
l=[1,2,3,4,5]
odd_even=list(map(lambda x:"even" if x%2==0 else 'odd',l))
print(odd_even)
# filter
#print numbers which less then 7
l=[3,4,6,44,100, 5, 3, 2]
x=list(filter(lambda x: x<7,l))
print(x)

#reduse
import functools
minimum=functools.reduce(lambda x, y: x if x<y else y,l)
print(minimum)