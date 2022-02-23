from django.urls import path
from . import views
from core.views import (
    AboutView, ContactCreateView, 
    CurriculumListView, FaqQuestionListView,MainListView,
    CourseView
)
app_name = 'core'

urlpatterns = [
    path("", MainListView.as_view(), name="index"),
    path("course/", CourseView.as_view(), name="course"),
    path('register/',views.register,name='register'),
    path("curriculum/", CurriculumListView.as_view(), name="curriculum"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactCreateView.as_view(), name="contact"),
    path("faq/", FaqQuestionListView.as_view(), name="faq"),
    
    
]
