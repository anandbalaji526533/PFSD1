from django.shortcuts import render
from .models import Feedback
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,View

def feedbackform(request):
    if request.method == 'POST':
        # Handle form submission
        Firstname = request.POST.get('First name')
        Lastname = request.POST.get('last name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        feedback = Feedback(Firstname=Firstname,Lastname=Lastname, email=email, phone=phone, comments=comments)
        feedback.save()
        # Redirect to a thank you page or display a thank you message
        return render(request, 'thank_you.html')
    else:
        # Display the feedback form
        return render(request, 'feedbackform.html')

# Class-based view for feedback form (using Django's CreateView)
class FeedbackFormView(CreateView):
    model = Feedback
    template_name = 'feedbackform.html'
    fields = ['Firstname','Lastname', 'email', 'phone', 'comments']
    success_url = reverse_lazy('thank_you')  # Redirect to thank you page after successful form submission


class ThankYouView(View):
    def get(self,request):
        return render(request, 'thank_you.html')