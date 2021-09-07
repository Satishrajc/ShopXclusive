from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path(r'', views.HomeView.as_view(), name='homepage'),
    path(r'add_products/', views.AddProducts.as_view(), name='add'),
    path(r'list/', views.ProductListView.as_view(), name='list'),
    path(r'detail/<int:pk>/', views.ProductDetailsView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete')
]