#c# ch05py(ch05 모듈)
# ctrl + shift + p => select interpreter을 이용해서 인터프리터(base) 선택
# 실행: cmd (ctrl+ j)에서 python ch05.py
def my_hello(cnt):
    print(__name__)
    for i in range(cnt):
        print('hello', 'python',end='\t')
        print('hello', 'world')
    
if __name__ == '__main__':
    my_hello(2)