from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
import secrets
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404,  redirect
from audioop import reverse


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет. перейти по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    return redirect(reverse("users:login"))
