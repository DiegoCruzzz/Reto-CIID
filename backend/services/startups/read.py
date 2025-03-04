from database.models import Startup

def get_all_startups():
    return Startup.query.all()


def get_startup_by_id(startup_id):
    return Startup.query.get_or_404(startup_id)