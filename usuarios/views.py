from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from usuarios.forms import RegisterForm


class UserRegistration(FormView):
    template_name = 'usuarios/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('usuarios:succeess')

    def form_valid(self,form):
        form.save()
        return super(UserRegistration, self).form_valid(form)
