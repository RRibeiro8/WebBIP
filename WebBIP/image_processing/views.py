from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class ImageProcessingView(View):

    template_name = 'image_processing/index.html'

    def get(self, request):
    

        context = {}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        print("POST")

        return JsonResponse({"success": True}, status=200)

