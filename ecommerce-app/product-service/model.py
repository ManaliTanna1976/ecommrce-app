from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    version = db.Column(db.Integer, nullable=False, default=0)

    __mapper_args__ = {
        "version_id_col": version,
        "version_id_generator": False
    }
