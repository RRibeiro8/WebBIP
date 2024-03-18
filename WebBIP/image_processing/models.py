from django.db import models


def get_upload_path(instance, filename):
    return "{0}".format(filename)


class ImageModel(models.Model):

    file = models.ImageField(upload_to=get_upload_path) 
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.name:
            self.name =  self.file.name.split('.')[0]

        super(ImageModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        self.file.delete()
        super(ImageModel, self).delete(*args, **kwargs)
