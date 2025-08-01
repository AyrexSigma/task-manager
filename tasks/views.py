from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task-list')