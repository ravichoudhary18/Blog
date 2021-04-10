from django.urls import path
from .views import HomeView, AboutView, ContactView, profile, BlogDetail, SettingView, profilupdate, Account_Deleted, AddPostView


urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("user/<str:username>/", profile, name='profile'),
    path("user/<str:username>/update/", profilupdate, name='profile_update'),
    path('user/<str:username>/account-deleted/', Account_Deleted, name="delete-account"),
    path("<str:slug>/", BlogDetail.as_view(), name="blog_detail"),
]
