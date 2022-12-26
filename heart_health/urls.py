
from django.urls import path

from . import views

app_name = 'heart_health'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('survey', views.survey, name='survey'),
    path('outcome', views.outcome, name='outcome'),
    path('education', views.education, name='education'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote')

]