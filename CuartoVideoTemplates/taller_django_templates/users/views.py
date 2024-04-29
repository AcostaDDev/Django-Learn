from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


class UserView(View):

    def get(self, request):
        users = User.objects.all()

        return render(request, 'user_list.html', {'users': users})
    
class UserDetailView(View):

    def get(self, request, pk):
        user = User.objects.get(id=pk)

        return render(request, 'user_detail.html', {'user': user})