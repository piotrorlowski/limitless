from django.views.generic.base import TemplateView


class ProfileAppView(TemplateView):
    template_name = "users/profile.html"
