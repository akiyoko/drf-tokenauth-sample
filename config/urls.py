from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from apiv1 import views as apiv1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('djoser-auth/', include('djoser.urls')),
    path('djoser-auth/', include('djoser.urls.authtoken')),

    path('api/v1/books/', apiv1_views.BookListCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', apiv1_views.BookRetrieveUpdateDestroyAPIView.as_view()),
]
