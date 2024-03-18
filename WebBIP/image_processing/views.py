from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import ImageModel


class ImageProcessingView(View):

    template_name = 'image_processing/index.html'

    def get(self, request):

        context = {"images": ImageModel.objects.all()}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        print("POST", request)

        file = request.FILES.get('image')
        print("Request: ", file) 

        name = file.name.split('.')[0]

        print(name)

        image, created = ImageModel.objects.get_or_create(file=file, name=name)


        return JsonResponse({"success": True}, status=200)

