from app import db
from passgen import passgen


def identifier(string_length):
    random_string = passgen(length=string_length, punctuation=False,
                            digits=True, letters=True, case='upper')
    return random_string


class User(db.Model):
    __abstract__ = True

    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    phone = db.Column(db.String(15))
    password_hash = db.Column(db.String(256))


class Employee(User):  # class A employee is a type of User
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    individual_client_id = db.relationship('IndividualClient', backref=db.backref('employee', lazy='dynamic'),
                                           lazy='dynamic', uselist=False)
    corp_client_id = db.relationship('CorporateClient', backref=db.backref('employee', lazy='dynamic'),
                                     lazy='dynamic', uselist=False)
    contact_id = db.relationship('Contact', backref=db.backref('employee', lazy='dynamic'),
                                 lazy='dynamic', uselist=False)

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class SelfService(User):  # class A employee is a type of User
    __tablename__ = 'self_service'

    id = db.Column(db.Integer, primary_key=True)
    individual_client_id = db.relationship('IndividualClient', backref=db.backref('self_service', lazy='dynamic'),
                                      lazy='dynamic', uselist=False)
    corporate_client_id = db.relationship('CorporateClient', backref=db.backref('self_service', lazy='dynamic'),
                                     lazy='dynamic', uselist=False)
    contact_id = db.relationship('Contact', backref=db.backref('self_service', lazy='dynamic'),
                                 lazy='dynamic', uselist=False)

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class Agent(User):  # class A
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    individual_client_id = db.relationship('IndividualClient', backref=db.backref('agent', lazy='dynamic'),
                                           lazy='dynamic', uselist=False)
    corporate_client_id = db.relationship('CorporateClient', backref=db.backref('agent', lazy='dynamic'),
                                          lazy='dynamic', uselist=False)
    contact_id = db.relationship('Contact', backref=db.backref('agent', lazy='dynamic'),
                                 lazy='dynamic', uselist=False)

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class Client(db.Model):  # class A
    __abstract__ = True

    title = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(15))


class IndividualClient(Client):  # class A individual client is a type of User
    __tablename__ = 'individual_clients'

    id = db.Column(db.Integer, primary_key=True)
    bvn = db.Column(db.String(11))
    client_class = db.Column(db.String(10))

    contact = db.relationship('ContactDetails',
                              backref=db.backref('individual_client', lazy='dynamic'),
                              lazy='dynamic')
    kyc_id = db.relationship('KYC',
                             backref=db.backref('individual_clients', lazy='dynamic'),
                             lazy='dynamic')
    portfolios = db.relationship('IndividualClient',
                                 backref=db.backref('individual_clients', lazy='dynamic'),
                                 lazy='dynamic', uselist=False)
    running_investment = db.relationship('Investment',
                                         backref=db.backref('individual_client', lazy='dynamic'),
                                         lazy='dynamic')

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class CorporateClient(Client):  # class A
    __tablename__ = 'corporate_clients'

    id = db.Column(db.Integer, primary_key=True)
    bvn = db.Column(db.String(11))
    client_class = db.Column(db.String(10))

    contact = db.relationship('ContactDetails', backref=db.backref('corporate_clients', lazy='dynamic'),
                              lazy='dynamic')
    kyc_id = db.relationship('KYC', backref=db.backref('corporate_clients', lazy='dynamic'),
                             lazy='dynamic')
    portfolios = db.relationship('Portfolio', backref=db.backref('corporate_clients', lazy='dynamic'),
                                 lazy='dynamic', uselist=False)
    running_investment = db.relationship('Investment',
                                         backref=db.backref('corporate_clients', lazy='dynamic'),
                                         lazy='dynamic')

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class ContactDetails(db.Model):  # class D all types of clients and user can have one or more contact details
    __tablename__ = 'contact_details'

    id = db.Column(db.Integer, primary_key=True)
    address_1 = db.Column(db.Text)
    address_2 = db.Column(db.Text)
    country = db.Column(db.String(20))
    state = db.Column(db.Text)
    individual_owner_id = db.Column(db.Integer, db.ForeignKey('individual_clients.id'))
    corporate_owner_id = db.Column(db.Integer, db.ForeignKey('corporate_clients.id'))
    agents_owner_id = db.Column(db.Integer, db.ForeignKey('agents.id'))


class KYC(db.Model):  # class A
    __tablename__ = 'kyc'

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.String(15))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
    individual_client = db.Column(db.Integer, db.ForeignKey('individual_clients.id'))
    corporate_client = db.Column(db.Integer, db.ForeignKey('corporate_clients.id'))

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class Portfolio(db.Model):  # class B
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    individual_client_id = db.Column(db.Integer, db.ForeignKey('individual_clients.id'))
    corporate_client_id = db.Column(db.Integer, db.ForeignKey('corporate_clients.id'))

    investments_products = db.relationship('Investment',
                                           backref=db.backref('portfolio', lazy='dynamic'),
                                           lazy='dynamic')

    def __repr__(self):
        return f'{self.individual_client_id} ,{self.corporate_client_id}'


class Investment(db.Model):  # class C  #an instance of product
    __tablename__ = 'investments'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rates = db.Column(db.Integer, db.ForeignKey('clients'))


class InvestmentManager(db.Model):  # class F  to manage existing investments
    __tablename__ = 'investment_manager'

    id = db.Column(db.Integer, primary_key=True)
    investment = db.Column(db.Integer, db.ForeignKey('investments.id'))


class Product(db.Model):  # abstract base model for products on the system
    __abstract__ = True

    product_name = db.Column(db.String(30))
    short_code = db.Column(db.String(15))
    desc = db.Column(db.String(100))
    # ...
    # rules = db.relationship("Rules", backref="products", lazy="select", uselist=False)


class MoneyMarketNote(Product):  # class A
    __tablename__ = 'money_market_notes'

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.String(15))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))

    # client_id = db.relationship('Client', backref=db.backref('clients', lazy='dynamic'),
                                 # lazy='dynamic', uselist=False)
    # running_investment = db.relationship('Investment', backref='investment_plan')

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class Retirement(Product):  # class A
    __tablename__ = 'retirement'

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.String(15))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))

    # client_id = db.relationship('IndividualClient', backref=db.backref('retirement_plan', lazy='dynamic'),
                                   # lazy='dynamic', uselist=False)
    # client_id = db.relationship('Client', backref=db.backref('clients', lazy='dynamic'),
                                 # lazy='dynamic', uselist=False)
    # running_investment = db.relationship('Investment', backref='investment_plan')

    def __repr__(self):
        return f'{self.name} ,{self.email}'


class Rules(db.Model):  # use to determine the unique behavior of each product
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    short_name = db.Column(db.String)
    description = db.Column(db.String)
    currency_code = db.Column(db.String)
    digits_after_decimal = db.Column(db.String)
    in_multiples_of = db.Column(db.String)
    interest_compounding_period_type = db.Column(db.String)
    interest_calculation_type = db.Column(db.String)
    interest_calculation_days_in_year_type = db.Column(db.String)
    min_deposit_term = db.Column(db.String)
    min_deposit_term_type_id = db.Column(db.String)
    accounting_rule = db.Column(db.String)
    min_tenor = db.Column(db.Integer)

    # ...
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))


class Rates(db.Model):  # class   to determine the rate
    __tablename__ = 'rates'

    id = db.Column(db.Integer, primary_key=True)
    investment_product = db.Column(db.Integer, db.ForeignKey('investments.id'))
