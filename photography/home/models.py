from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class UploadedImage(models.Model):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
