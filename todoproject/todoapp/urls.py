from .import views
from django.urls import path
appname='todoapp'
urlpatterns = [

    path('',views.add,name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')

]
