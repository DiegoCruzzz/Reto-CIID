from database.db import db
from database.models import Startup
from database.models import Technology
from datetime import datetime

def create_startup(data):
    founded_date = datetime.strptime(data.get('founded_date'), '%Y-%m-%d').date() if data.get('founded_date') else None

    new_startup = Startup(
        name=data.get('name'),
        description=data.get('description'),
        founded_date=founded_date,
        website=data.get('website'),
        country=data.get('country'),
    )

    if 'technologies' in data:
        tech_ids = data['technologies']
        new_startup.technologies = Technology.query.filter(Technology.id.in_(tech_ids)).all()

    db.session.add(new_startup)
    db.session.commit()
    return new_startup

