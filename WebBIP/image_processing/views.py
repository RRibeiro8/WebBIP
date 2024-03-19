from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import ImageModel

from django.core.files.storage import FileSystemStorage
from django.core.files import File

from PIL import Image, ImageEnhance

import io


class ImageProcessingView(View):

    template_name = 'image_processing/index.html'

    def get(self, request):

        context = {"images": ImageModel.objects.all()}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

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

            pk = request.POST.getlist('pk')[0]

            image = ImageModel.objects.filter(pk=pk).first()

            if image:

                if method == "selected":

                    context = { "success": True,
                            "id": "original", 
                            "img_path": image.file.url}

                    return JsonResponse(context, status=200)

                elif method == "processing":

                    contrast = int(request.POST.getlist('filters[contrast]')[0])
                    brightness = int(request.POST.getlist('filters[brightness]')[0])

                    name = "processed.png"

                    fs = FileSystemStorage()
                    if fs.exists(name):
                        fs.delete(name)

                    img = Image.open(image.file)

                    enhancer = ImageEnhance.Contrast(img)
                    contrast = contrast/127+1
                    img = enhancer.enhance(contrast)



                    enhancer = ImageEnhance.Brightness(img)
                    brightness = brightness/127+1
                    img = enhancer.enhance(brightness)


                    if request.POST.getlist('filters[rotate90]')[0] == "true":
                        img = img.transpose(Image.ROTATE_90)

                    if request.POST.getlist('filters[rotate180]')[0] == "true":
                        img = img.transpose(Image.ROTATE_180)

                    if request.POST.getlist('filters[flipv]')[0] == "true":
                        img = img.transpose(Image.FLIP_TOP_BOTTOM)

                    if request.POST.getlist('filters[fliph]')[0] == "true":
                        img = img.transpose(Image.FLIP_LEFT_RIGHT)



                    img_output = io.BytesIO()
                    img.save(img_output, 'PNG')

                    img_file = fs.save(name, File(img_output, name=name))
                    fileurl = fs.url(img_file)
                    
                    context = { "success": True, 
                                "id": "processed",
                                "img_path": fileurl}

                    return JsonResponse(context, status=200)

        
        return JsonResponse({"success": False}, status=400)

