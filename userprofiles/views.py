from django.shortcuts import render

from django.views.generic import View, TemplateView
from django.http import HttpResponse

# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Esto es una vista basado en Clases!!!')

class LoginView(TemplateView):
    template_name = 'login.html'

    # Sobreescribir el get_context_data para que haga otras cosas
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        username = None

        if self.request.user.is_authenticated():
            is_auth = True
            username = self.request.user.username

        context.update({'is_auth': is_auth , 'username': username})
        return context

