from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('institucion/', HomePageView.as_view(), name="institucion"),
    path('alumnos/centro-de-estudiantes', HomePageView.as_view(), name="alumnos_centro-de-estudiantes"),
    path('alumnos/inscripciones', HomePageView.as_view(), name="alumnos_inscripciones"),
    path('alumnos/examenes', HomePageView.as_view(), name="alumnos_examenes"),
    path('alumnos/horarios', HomePageView.as_view(), name="alumnos_horarios"),
    path('alumnos/modalidades', HomePageView.as_view(), name="alumnos_horarios"),
]