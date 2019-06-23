from apel_apvest.base import db


class Product(db):
    #
    __tablename__ = 'product'

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

    def __repr__(self):
        pass

    class Rates(db):
        __tablename='rates'

        def create_rate(self, props):
            pass

        def set_properties(self, props, effect_date):
            pass

        def delete_properties(self, props, effect_date):
            pass

        def properties(self, props):
            pass

        def __repr__(self):
            pass

    class Rules(db):
        __tablename='rules'

        def create_rule(self, props):
            pass

        def set_properties(self, props, effect_date):
            pass

        def delete_properties(self, props, effect_date):
            pass

        def properties(self, props):
            pass

        def __repr__(self):
            pass
