from django.shortcuts import redirect, render

from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.views import View

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy

from django.db import transaction

from .forms import *
from . models import Task



class TempView(TemplateView):
    template_name = "home.html"

class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self) -> str    :
        return reverse_lazy('base:tasks')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base:tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task    # => task_form.html
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:tasks')
    login_url = reverse_lazy('base:login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    login_url = reverse_lazy('base:login')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'
    login_url = reverse_lazy('base:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)
        context['search_input'] = search_input

        return context
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:tasks')
    login_url = reverse_lazy('base:login')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:tasks')
    login_url = reverse_lazy('base:login')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
    

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['position'])
            
            position_list = form.cleaned_data['position'].split(',')
            print(position_list)

            with transaction.atomic():
                self.request.user.set_task_order(position_list)
        
        return redirect(reverse_lazy('base:tasks'))
    
def custom_404(request, exception):
    return render(request, '404.html', status=404)