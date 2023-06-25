from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='image/')
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        return reverse('books:book_details', args=[self.slug])

    def __str__(self):
        return self.title
