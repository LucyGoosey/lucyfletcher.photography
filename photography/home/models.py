from django.db import models

from modelcluster.fields import ParentalKey

from taggit.models import Tag

from django.contrib.contenttypes.models import ContentType

from wagtail.core.models import Page, Orderable
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('featured_photos', label='Photos'),
    ]


class HomePageModel(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='featured_photos')
    photo_page = models.ForeignKey(
        'PhotoPage',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    panels = [
        PageChooserPanel('photo_page')
    ]


class GalleryPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('photo_pages', label='Photos'),
    ]

    tags = Tag.objects.all()


class GalleryModel(Orderable):
    page = ParentalKey(GalleryPage, on_delete=models.CASCADE, related_name='photo_pages')
    photo_page = models.ForeignKey(
        'PhotoPage',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    panels = [
        PageChooserPanel('photo_page')
    ]


class PhotoPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('photo', label='Photo', max_num=1),
    ]


class UploadedImage(Orderable):
    page = ParentalKey(PhotoPage, on_delete=models.CASCADE, related_name='photo')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]