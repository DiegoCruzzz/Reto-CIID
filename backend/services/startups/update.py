from database.db import db
from database.models import Startup
from database.models import Technology
from datetime import datetime

def update_startup(startup_id, data):
    startup = Startup.query.get_or_404(startup_id)
    startup.name = data.get('name', startup.name)
    startup.description = data.get('description', startup.description)
    startup.founded_date = datetime.strptime(data.get('founded_date'), '%Y-%m-%d').date() if data.get(
        'founded_date') else startup.founded_date
    startup.website = data.get('website', startup.website)
    startup.country = data.get('country', startup.country)

    if 'technologies' in data:
        tech_ids = data['technologies']
        startup.technologies = Technology.query.filter(Technology.id.in_(tech_ids)).all()

    db.session.commit()
    return startup