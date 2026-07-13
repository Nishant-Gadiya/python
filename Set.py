numbers=[x for x in range(1,6)]

sq=list(map(lambda x:x*x,numbers))

even = list(filter(lambda x:x%2==0,numbers))

def fun(*nums):
    print(sum(nums))


def f(**k):
    for c,v in k.items():
        print(c,v)

print(sq)
print(even)
fun(1,2,3,4,5)
f(a="b",c="d",e="f")