from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView 
from .forms import NewUserForm
from django.urls import reverse_lazy


class RegistrationView(CreateView):
    form_class = NewUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')
    success_message = "Your profile was created successfully"


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.user
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)