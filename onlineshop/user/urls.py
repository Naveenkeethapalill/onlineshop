from django .urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('signin',views.signin, name='signin'),
    path('cart',views.cart,name='cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    #path('cart/item_clear/<int:id>/', views.cart_clear, name='item_clear'),
    #path('cart/item_increment/<int:id>/',
    #      views.item_increment, name='item_increment'),
    #path('cart/item_decrement/<int:id>/',
    #      views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('readmore/<int:id>/',views.readmore, name='readmore'),
 ]