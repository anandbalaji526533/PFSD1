from django.urls import path
from . import views

urlpatterns = [

    path('feedbackform/', views.FeedbackFormView.as_view(), name='feedbackform'),
    path('feedbackform/thank_you/', views.ThankYouView.as_view(), name='thank_you'),
]