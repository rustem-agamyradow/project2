from django.urls import path
from . import views


urlpatterns = [
    path('',views.courses_list, name='courses.html'),
    path('<slug:category_slug>/<int:course_id>',views.course_detail, name='course_detail.html'),
    path('categories/<slug:category_slug>',views.category_detail, name='courses_by_category.html'),


]