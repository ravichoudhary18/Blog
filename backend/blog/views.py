from .forms import ContectForm, UsernameUpdateForm, UserUpdateForm, ProfileUpdateForm,AddBlogFroms
from django.views.generic import FormView, ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from authentication.models import Profile
from django.urls import reverse_lazy
from .models import Blog


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'
    ordering = ['-Timestamp']

class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['latest_post'] = Blog.objects.order_by('-Timestamp')[:3]
        context['trending_now'] = Blog.objects.order_by('-views_count')[:3]
        return context

    def get_object(self):
        object = super(BlogDetail, self).get_object()
        object.views_count = object.views_count +1 
        object.save()
        return object


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(FormView):
    form_class = ContectForm
    template_name = "contact.html"
    success_url="/contact"

    def post(self, request):
        form = ContectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank You for Contact')
            return redirect('/')
        return render(request, '/', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.user 
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)


@login_required
def profilupdate(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile_update.html', context)



class SettingView(TemplateView):
    template_name = "setting.html"
    form_class = UsernameUpdateForm
    model = User

    def post(self, request):
        u_form = UsernameUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('setting')

        else:
            u_form = UsernameUpdateForm(instance=request.user)

        context = {
            'u_form': u_form,
        }

        return render(request, 'setting.html', context)


@login_required
def Account_Deleted(request,username):
    if request.method == "POST":
        u = User.objects.get(
            username = request.username)
        u.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect('/')
    return redirect(request, 'delete-account.html')


class AddPostView(LoginRequiredMixin,FormView):
    template_name = 'add-post.html'
    form_class = AddBlogFroms
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddBookForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
            messages.success(request, f'Add New Blog Success Fully')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})