from django.urls import path, include
from .views import HomePageView, InstitucionPageView, SecretariaPageView, ContactoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('institucion/', InstitucionPageView.as_view(), name="institucion"),
    path('alumnos/centro-de-estudiantes', HomePageView.as_view(), name="alumnos_centro-de-estudiantes"),
    path('alumnos/inscripciones', HomePageView.as_view(), name="alumnos_inscripciones"),
    path('alumnos/examenes', HomePageView.as_view(), name="alumnos_examenes"),
    path('alumnos/horarios', HomePageView.as_view(), name="alumnos_horarios"),
    path('alumnos/modalidades/', include('modalidades.urls')),
    path('biblioteca', include('libros.urls')),
    path('secretaria/', SecretariaPageView.as_view(), name='secretaria'),
    path('contacto/', ContactoPageView.as_view(), name='contacto')
]