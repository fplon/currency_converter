from flask import abort, make_response

from config import db
from models import Rate, rates_schema, rate_schema


def read_all():
    rates = Rate.query.all()
    return rates_schema.dump(rates)

def create(rate, ccy_code): 
    rate_date = rate.get('rate_date')
    ccy_code = rate.get('ccy_code')
    existing_rate = Rate.query.filter(
        Rate.rate_date == rate_date, Rate.ccy_code == ccy_code).one_or_none()

    if existing_rate is None:
        new_rate = rate_schema.load(rate, session=db.session)
        db.session.add(new_rate)
        db.session.commit()
        return rate_schema.dump(new_rate), 201
    else: 
        abort(
            406, 
            f"Rate with date {rate_date} already exists"
        )

def read_one(rate_date, ccy_code): 
    rate = Rate.query.filter(
        Rate.rate_date == rate_date,
        Rate.ccy_code == ccy_code).one_or_none()

    if rate is not None: 
        return rate_schema.dump(rate)
    else: 
        abort(
            404, 
            f"Rate with date {rate_date} not found"
        )

def update(rate_date, ccy_code, rate):
    existing_rate = Rate.query.filter(
        Rate.rate_date == rate_date, Rate.ccy_code == ccy_code).one_or_none()

    if existing_rate:
        update_rate = rate_schema.load(rate, session=db.session)
        existing_rate.rate = update_rate.rate
        db.session.merge(existing_rate)
        db.session.commit()
        return rate_schema.dump(existing_rate), 201
    else:
        abort(
            404,
            f"Rate with date {rate_date} not found"
        )

def delete(rate_date, ccy_code):
    existing_rate = Rate.query.filter(
        Rate.rate_date == rate_date, Rate.ccy_code == ccy_code).one_or_none()

    if existing_rate:
        db.session.delete(existing_rate)
        db.session.commit()
        return make_response(f"{rate_date} successfully deleted", 200)
    else:
        abort(
            404,
            f"Rate with date {rate_date} not found"
        )