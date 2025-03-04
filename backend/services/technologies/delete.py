from database.db import db
from database.models import Technology

def delete_technology(tech_id):
    technology = Technology.query.get_or_404(tech_id)
    db.session.delete(technology)
    db.session.commit()
