from database.models import Technology

def get_all_technologies():
    return Technology.query.all()

def get_technology_by_id(tech_id):
    return Technology.query.get_or_404(tech_id)
