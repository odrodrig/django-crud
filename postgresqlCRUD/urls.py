from django.conf.urls import url

from postgresqlCRUD import views

urlpatterns = [
  url(r'^$', views.PeopleList.as_view(), name='people_list'),
  url(r'^new$', views.PeopleCreate.as_view(), name='people_new'),
  url(r'^edit/(?P<pk>\d+)$', views.PeopleUpdate.as_view(), name='people_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.PeopleDelete.as_view(), name='people_delete'),
]
