def func(st,x):
    tmp=st.replace('x',str(x))
    return(eval(tmp))

#a,b는 해가 위치하는 구간, x는 소숫점 아래 유효숫자, func는 함수
def regula_falsi(a,b,x,calc):
    ans=0
    pre=0
    i=1
    while(True):
        ans=(a*func(calc,b)-b*func(calc,a))/(func(calc,b)-func(calc,a))
        if (func(calc,ans)<0):
            a=ans
        else:
            b=ans
        if (abs(ans-pre)<1/10**x):
            print(ans)
            break
        print(ans)
        pre=ans
        i+=1
print("계산할 함수를 입력하세요())>>")
calc=input()
print("해의 유효숫자를 입력하세요>>")
num=int(input())
print("해가 존재할거라고 예상되는 구간을 입력하세요")
x,y=map(int,input().split())
regula_falsi(x,y,num,calc) if func(calc, x)<0 else regula_falsi(y,x,num,calc)