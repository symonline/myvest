from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    '''
    Defining new investment product on the system
    Template for various Types of Investments Product
    '''

    @abstractmethod
    def create_product(self, props):
        pass

    @abstractmethod
    def set_properties(self, props, effect_date):
        pass

    @abstractmethod
    def properties(self, props):
        pass

    # def __repr__(self):
        # pass


class MoneyMarketInvestment(Product):
    #
    __product_list__ = []

    def __init__(self, *args, **kwargs):
        self.args = args
        self.args = kwargs

    def create_product(self, props):
        pass

    def set_properties(self, props, effect_date):
        pass

    def delete_properties(self, props, effect_date):
        pass

    def properties(self, props):
        pass


class InvestmentManager(metaclass=ABCMeta):
    # Template for MoneyMarket Investments Product Factory

    @abstractmethod
    def rollover_inv(self, inv):
        pass

    @abstractmethod
    def terminate_inv(self, inv):
        pass

    @abstractmethod
    def suspend_inv(self, inv):
        pass

    def __repr__(self):
        pass

