from django.contrib import admin
from django.urls import path
from todo.views import add_todo, all_todos, complete_todo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add-todo/", add_todo),
    path("todos/", all_todos, name='todos'),
    path("complete-todo/<int:id>", complete_todo, name='complete_todo')
]
