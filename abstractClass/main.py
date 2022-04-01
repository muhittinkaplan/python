from abc import ABC, abstractmethod#builtin bir modüldür.

class AbstractClassExample(ABC):

    @abstractmethod #alt sınıfta kesinlikle tanımlanması gereken methodların üzerine @abstractmethod dekoratörünü eklenir
    def do_something(self):
        print("Some implementation!")


class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()  # üst sınıfın fonksiyonu çağrılıyor
        print("The enrichment from AnotherSubclass")

x = AnotherSubclass()
x.do_something()
