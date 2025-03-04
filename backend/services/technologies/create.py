from database.db import db
from database.models import Technology

def create_technology(data):
    new_technology = Technology(
        name=data.get('name'),
        description=data.get('description'),
    )

    db.session.add(new_technology)
    db.session.commit()
    return new_technology
