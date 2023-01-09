from datetime import datetime
from config import db, ma

class Rate(db.Model): 
    __tablename__ = 'rate'
    id = db.Column(db.Integer, primary_key=True)
    ccy_code = db.Column(db.String(3), unique=False, nullable=False)
    rate_date = db.Column(db.String(10), unique=False, nullable=False)
    rate = db.Column(db.Float(precision=6), unique=False, nullable=False)

class RateSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Rate
        load_instance = True
        sqla_session = db.session

rate_schema = RateSchema()
rates_schema = RateSchema(many=True)