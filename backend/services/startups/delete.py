from database.db import db
from database.models import Startup

def delete_startup(startup_id):
    startup = Startup.query.get_or_404(startup_id)
    db.session.delete(startup)
    db.session.commit()
