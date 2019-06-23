from app import db


class Contact(db.Model):
    __tablename='contact'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    email = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    address_1 = db.Column(db.String(32))
    address_2 = db.Column(db.String(32))
    country = db.Column(db.String(32))
    state = db.Column(db.String(32))
    creation_date = db.Column(db.Date)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)

    def create_contact(self, props):
        pass

    def set_properties(self, props, effect_date):
        pass

    def delete_properties(self, props, effect_date):
        pass

    def properties(self, props):
        pass

    def __repr__(self):
        return f'{self.address_1},{self.address_2}'