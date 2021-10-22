from Apps.share.horarioMedico.views import HorarioMedicoView
from Apps.share.medico.viewsets import MedicoViewset
from rest_framework import routers

router = routers.DefaultRouter()

# Registrar las rutas
router.register('medico', MedicoViewset)
router.register('horarioMedico', HorarioMedicoView)

# Localhost:p/api/medico/5
# GET, POST, UPDATE , DELETE