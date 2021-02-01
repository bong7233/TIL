# class
# OPP(객체 지향 프로그래밍)
# class instance
# self 개념
# instance method

# class 와 instance의 차이를 이해 point
# 인스턴스와 객체의 차이점을 찾아서 이해하기 필수
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공(dict형태)
# 클래스변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재 
# ex
class Dog(object): #(object) 이건 생략가능
# Dog, Dog(), Dog(object) 는 같다
    # 클래스의 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b) #NO

# 네임스페이스
print('dog1',a.__dict__)
print('dog1',b.__dict__)
