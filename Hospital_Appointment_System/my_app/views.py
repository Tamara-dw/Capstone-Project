# main_app/views.py
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Appointment,Doctor
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AppointmentForm

# Home page with login form
class Home(LoginView):
    template_name = 'my_app/home.html'

def about(request):
    return render(request, 'my_app/about.html')

# Sign up view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            return redirect('home')  # redirect after signup, يمكن تغييره لاحقًا
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    return render(request, 'my_app/signup.html', {'form': form, 'error_message': error_message})

class DashboardView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'my_app/dashboard.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user).order_by('appointment_datetime')


    
class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm  # الفورم للموعد

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class AppointmentUpdate(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm  # نفس الفورم المستخدم لإنشاء الموعد

    def get_queryset(self):
        # يسمح للمستخدم فقط بتعديل مواعيده الخاصة
        return Appointment.objects.filter(patient=self.request.user)

    def get_success_url(self):
        return reverse('dashboard')

class AppointmentDelete(LoginRequiredMixin, DeleteView):
    model = Appointment

    def get_queryset(self):
        # يسمح للمستخدم فقط بحذف مواعيده الخاصة
        return Appointment.objects.filter(patient=self.request.user)

    def get_success_url(self):
        return reverse_lazy('dashboard')




class DoctorListView(ListView):
    model = Doctor
    template_name = 'my_app/doctor_list.html'
    context_object_name = 'doctors'