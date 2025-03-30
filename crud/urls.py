from django.urls import path,include
from .import views
urlpatterns = [
   path("",views.InsertPageView,name='insert.html'),
   path("insert/", views.InsertData, name='insert'),
   path('showdata/',views.ShowData, name='showdata'),
   path('editpage/<int:pk>',views.EditPage, name='editpage'),
   path('updatedata/<int:pk>',views.UpdateData, name='updatedata'),
   path('deletedata/<int:pk>',views.DeleteData, name='deletedata'),
]
