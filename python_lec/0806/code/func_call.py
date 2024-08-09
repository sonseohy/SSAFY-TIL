def func1(a):
    func2(a)
    a += 1
    print('func1', a)
def func2(a):
    print('func2', a)

a = 3
print('main', a)
func1(a)
print('main', a)