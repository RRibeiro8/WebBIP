from django.urls import path
from image_processing.views import ImageProcessingView

urlpatterns = [

    path('', ImageProcessingView.as_view(), name='images-processing'),

]