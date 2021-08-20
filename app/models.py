from os import name
from app import db, login

from flask import render_template
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(240), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class CallRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), index=True, nullable=False)
    name = db.Column(db.String(300), index=True, nullable=False)
    email = db.Column(db.String(150), index=True)
    comment = db.Column(db.Text)

    def __repr__(self): 
        return render_template('parts/call-request.html', req=self)


class NamedSource():
    def __repr__(self):
        return self.name


class PriceType(NamedSource, db.Model):
    __admin_name__ = 'Типы занятий'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), index=True, nullable=False)

    prices = db.relationship('Price', backref='type', lazy='dynamic')

class PricePeriod(NamedSource, db.Model):
    __admin_name__ = "Периоды оплаты"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), index=True, nullable=False)
    min = db.Column(db.Integer, default=1)
    is_for_beneficiary = db.Column(db.Boolean, default=False)

    prices = db.relationship('Price', backref='period', lazy='dynamic')

class PriceAge(NamedSource, db.Model):
    __admin_name__ = "Возрастные группы"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), index=True, nullable=False)

    prices = db.relationship('Price', backref='age', lazy='dynamic')

class Price(db.Model):
    __admin_name__ = "Цены"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('price_type.id', ondelete='RESTRICT'), index=True, nullable=False)
    period_id = db.Column(db.Integer, db.ForeignKey('price_period.id', ondelete='RESTRICT'), index=True, nullable=False)
    age_id = db.Column(db.Integer, db.ForeignKey('price_age.id', ondelete='RESTRICT'), index=True, nullable=False)
