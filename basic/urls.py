from collections import namedtuple
from django.urls import path
from basic import views
from basic.models import Student

result_list_view = views.Result.as_view(
    queryset = Student.objects.order_by("last_name")[:10],
    context_object_name ="student_list",
    template_name="basic/result.html",
)


urlpatterns = [
    path("result",result_list_view, name="result"),
    path("", views.home, name="home"),
]