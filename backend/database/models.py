from database.db import db
from datetime import datetime

startup_technologies = db.Table(
    'startup_technologies',
    db.Column('startup_id', db.Integer, db.ForeignKey('startup.id'), primary_key=True),
    db.Column('technology_id', db.Integer, db.ForeignKey('technology.id'), primary_key=True)
)

class Startup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    founded_date = db.Column(db.Date, nullable=True)
    website = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    technologies = db.relationship('Technology', secondary=startup_technologies, backref='startups')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "founded_date": self.founded_date.strftime('%Y-%m-%d') if self.founded_date else None,
            "website": self.website,
            "country": self.country,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "technologies": [tech.serialize() for tech in self.technologies]
        }

class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
