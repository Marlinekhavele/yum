# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView


# def emailView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')

class Homeview(LoginRequiredMixin , TemplateView):
    template_name='feed.html'

    def get(self,request):
        form = FeedbackForm()
        return render(request, "feed.html", {'form':form})
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name  = request.user
            post.save()
            phone = form.cleaned_data['phone']
            neighbourhood = form.cleaned_data['neighbourhood']
            rating = form.cleaned_data['rating']
            comments = form.cleaned_data['comments']
    


            form  = FeedbackForm()
            return redirect("home")
        args = {'form': form, "phone":phone,"neighbourhood":neighbourhood,"rating":rating,"comments":comments}
        return render(request, "feed.html", args)
