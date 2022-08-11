from django.shortcuts import render

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/task_list.html', {})
