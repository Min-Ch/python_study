class Fruit:
    def __init__(self, name, price):
        self.name = name
        self._price = self._validate_price(price)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = self._validate_price(price)

    def __attribs(self):
        attribs = [(k, v) for k, v in self.__dict__.items() if not k.startswith("_")]  # '_'로 시작하는 field 제거
        for name in dir(self.__class__):
            if name.startswith("_"):
                continue
            obj = getattr(self.__class__, name)
            if isinstance(obj, property):  # '_'로 시작하지 않고 property인 것들만 추출
                val = obj.__get__(self, self.__class__)
                attribs.append((name, val))
        return attribs

    def _validate_price(self, price):
        if price < 1000:
            raise ValueError('너무 쌉니다!')
        elif price > 10000:
            raise ValueError('너무 비쌉니다!')
        return price

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self)

    def __str__(self):
        return f"{self.name}, {self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price

    def __eq__(self, other):
        return self.__attribs() == other.__attribs()

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __iter__(self):
        yield from ((k,v) for k, v in self.__attribs())


if __name__ == '__main__':
    # 선언 및 표현
    f1 = Fruit(name='사과', price=1000)
    f2 = Fruit(name='수박', price=5000)
    f3 = Fruit(name='사과', price=3000)

    fruit_lst = [f1, f2, f3]

    # print('1. 표현 : __str__ vs __repr__')
    # print(f1)
    # print(f3)
    # print(fruit_lst)
    #
    # """
    # [정리]
    # __str__ => 서로 다른 데이터 타입이 상호작용하는 인터페이스 역할로 사용 (다른 데이터와 호환성 중요시) / formal(격식체)
    # __repr__ => 사람에게 객체를 이해할 수 있는 평문으로 표시하는 역할 / informal(비격식체, 구어체)
    # """

    # 크기 비교
    # f1.price = 3000
    #
    # print('\n2. 크기 비교 : __eq__, __lt__, __gt__ ..., 사칙 연산 : __add__, __sub__ ...')
    # print(f1 == f3)
    # print(f1 < f2)
    # print(f1 + f2)
    # print(f2 - f1)
    # print(sorted(fruit_lst))
    #
    # """
    # [정리]
    # 크기 비교하는 매직 메소드 (__eq__, __lt__, __gt__, __le__, __ge__)를 정의하면,
    # 객체간의 크기 비교와 정렬이 가능하다.
    # 마찬가지로 사칙 연산(__add__, __sub__ ...) 매직 메소드를 정의하면,
    # 객체간의 연산이 가능하다.
    # """
    #
    # dictionary 만들기
    print('\n3. __dict__와 dict()')

    f1_dict = dict(f1)
    a = f1.__dict__

    print(f1_dict, '-> dict()')
    print(a, '-> __dict__')

    f1.name = '바나나'
    f1.price = 9000

    print(f1_dict, '-> dict()')
    print(a, '-> __dict__')

    f4 = Fruit(**f1_dict)

    print(f4)

    print(f1 == f4)

    """
    [정리]
    __dict__를 이용하여 dictionary를 생성하게 되면,
    객체의 변수와 그 값을 dictionary 형태로 접근 가능하다.
    하지만 객체 변수와 생성된 dict의 key가 같은 메모리 주소(얕은 복사)를 바라보고 있다.(서로 영향을 받음)
    또, 객체 내에 있는 변수명으로 지정되기 때문에, property로 지정한 변수는 반환 하지 않는다.(위 경우에서는 price 대신에 _price)
    이를 해결하기 위해 객체를 이터러블하게 만들고, dict() 함수를 사용하게 되면
    property 변수를 사용할 수 있고 해당 객체의 영향을 받지 않는(깊은 복사) dictionary를 생성할 수 있다.
    """