from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.prematch, name='prematch'),
#    url(r'^$', views.upload_csv, name='upload_csv'),
]


#from .views import *

#urlpatterns = [
#   url(r'^$', index, name='index'),
#   url(r'^DataSet$', display_dataset, name="display_dataset"),
#   url(r'^simple_upload$', simple_upload, name="simple_upload"),
#   url(r'^prematch$', prematch, name="prematch"),

#   url(r'^add_dataset$', add_dataset, name="add_dataset"),

 #  url(r'^dataset/edit_item/(?P<pk>\d+)$', edit_dataset, name="edit_dataset"),

 #  url(r'^DataSet/delete/(?P<pk>\d+)$', delete_dataset, name="delete_dataset"),

#]
