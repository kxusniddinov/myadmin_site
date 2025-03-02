from django.urls import path
from .views import home_page, login_page, logout_page, SignUpView

urlpatterns = [
    path('', home_page, name="home_page"),
    path('login_page/', login_page, name="login_page"),
    path('logout_page/', logout_page, name="logout_page"),
    path('signup/', SignUpView.as_view(), name="signup"),

    path('faculty/create/', faculty_create, name='faculty_create'),
    path('faculty/<int:pk>/edit/', faculty_edit, name='faculty_edit'),
    path('faculty/<int:pk>/delete/', faculty_delete, name='faculty_delete'),
    path('faculty/list/', faculty_list, name='faculty_list'),

    path('chair/create/', chair_create, name='chair_create'),
    path('chair/<int:pk>/edit/', chair_edit, name='chair_edit'),
    path('chair/<int:pk>/delete/', chair_delete, name='chair_delete'),
    path('chair/list/', chair_list, name='chair_list'),
]