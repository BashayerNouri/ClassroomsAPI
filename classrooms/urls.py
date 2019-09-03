
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from app import views as api_views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('class/list/', api_views.ClassList.as_view(), name="class-list"), 
    path('class/detail/<int:class_id>/', api_views.ClassDetails.as_view(), name="class-details"),
    path('class/<int:class_id>/update/', api_views.UpdateClass.as_view(), name="update-class"),
    path('class/<int:class_id>/cancel/', api_views.CancelClass.as_view(), name="cancel-class"),
    path('class/create/', api_views.CreateClass.as_view(), name="create-class"),


]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
