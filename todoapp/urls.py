from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TasklistView.as_view(),name='cbvhome'),
    path('cdvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cdvdetail'),
    path('cdvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cdvupdate'),
path('cdvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cdvdelete')
]