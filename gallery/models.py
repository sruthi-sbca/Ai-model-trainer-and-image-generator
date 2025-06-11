from django.db import models

class GalleryItem(models.Model):
    image = models.ImageField(upload_to='', blank=False)       # Save directly to I:\images
    text_file = models.FileField(upload_to='', blank=False)    # Save directly to I:\images

    def __str__(self):
        return self.image.name

    @property
    def text_content(self):
        with open(self.text_file.path, 'r', encoding='utf-8') as f:
            return f.read()
