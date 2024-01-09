from django.urls import path
from . import views
from rest_framework.authtoken import views as authview
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('users',views.UserView.as_view()),

    path('menu-items',views.menu_items),
    path('menu-items/<int:pk>',views.menu_singleinfo.as_view()),
    path('category',views.category_items),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-auth/',authview.obtain_auth_token, name='api-token'),
    path('menu-items-v2',views.menuv2.as_view(
        {'get':'list','post':'create'}
    )),
    path('menu-items-v2/<int:pk>',views.menuv2.as_view(
        {
            'get':'retrive',
            'put':'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }
    )),
]