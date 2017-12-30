from django.conf.urls import url

from .views import BoardList, BoardDetail, CommentList, CommentDetail

urlpatterns = [
    url(r'^$', BoardList.as_view(), name=BoardList.name),
    url(r'^(?P<pk>[0-9]+)/$', BoardDetail.as_view(), name=BoardDetail.name),
    url(r'^comment/$', CommentList.as_view(), name=BoardList.name),
    url(r'^comment/(?P<pk>[0-9]+)/$', CommentDetail.as_view(), name=BoardDetail.name),
]
