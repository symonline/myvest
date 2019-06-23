from project.models import Employee, Agent, SelfService
from abc import ABCMeta, abstractmethod

#staff=Employee( username = 'Symonline', email = 'goldbars.ng@gmail.com', phone = db.Column(db.String(15)), password_hash = db.Column(db.String(256))

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_vegas_pizza(self):
    pass

    @abstractmethod
    def create_non_vegas_pizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):


    def create_vegas_pizza(self):
        return DeluxVeggiePizza()

    def create_non_vegas_pizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory):

    def create_vegas_pizza(self):
        return Mexicanvegas_pizza()

    def create_non_vegas_pizza(self):
        return HamPizza()