from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.auth import login, views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from reports_auth.forms import RegisterForm, ProfileForm, LoginForm


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'auth/register.html', context)


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
