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
        if file:

            name = file.name.split('.')[0]

            image, created = ImageModel.objects.get_or_create(file=file, name=name)

            context = { "success": True, 
                        "name": image.name,
                        "pk": image.pk}
            return JsonResponse(context, status=200)

        else:

            method = request.POST.getlist('method')[0]

            if method == "selected":

                pk = request.POST.getlist('pk')[0]

                image = ImageModel.objects.filter(pk=pk).first()

                if image:

                    context = { "success": True, 
                            "img_path": image.file.url}

                    return JsonResponse(context, safe=False, status=200)



        
        return JsonResponse({"success": False}, status=400)

