from database.db import db
from database.models import Technology

def update_technology(tech_id, data):
    technology = Technology.query.get_or_404(tech_id)

    if 'name' in data:
        technology.name = data['name']
    if 'description' in data:
        technology.description = data['description']

    db.session.commit()
    return technology
