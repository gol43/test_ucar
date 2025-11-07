from app.services.incedent_service import IncedentService
from app.database.models import Incedent


def incedents_services():
    return IncedentService(Incedent)