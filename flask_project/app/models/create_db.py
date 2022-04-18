from datetime import datetime
from app import db

class Tasks(db.Model): 
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_create = db.Column(db.DateTime, default=str(datetime.now())[0:19])

    def __repr__(self):
        return "<Task ID: %r>" % self.id