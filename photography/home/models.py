from django.db import models

from modelcluster.fields import ParentalKey

from taggit.models import Tag

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class InlineImage(Orderable):
    photo_page = models.ForeignKey(
        'PhotoPage',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    panels = [
        PageChooserPanel('photo_page')
    ]


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('featured_photos', label='Photos'),
    ]


class GalleryPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('photo_pages', label='Photos'),
    ]

    tags = Tag.objects.all()


class AboutPage(Page):
    name = models.TextField(
        verbose_name="Your Name",
        max_length=160,
        blank=False
    )
    descriptor = models.TextField(
        max_length=160,
        verbose_name='Your "job" title',
        blank=False
    )
    summary = models.TextField(
        verbose_name="Write a short bit about yourself",
        blank=False
    )
    location = models.TextField(
        verbose_name="Where are you based?",
        blank=True
    )
    email = models.TextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('descriptor'),
        FieldPanel('summary'),
        FieldPanel('location'),
        FieldPanel('email'),
        InlinePanel('personal_photo', label="Your Picture", max_num=1)
    ]


class HomePageModel(InlineImage):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='featured_photos')


class GalleryModel(InlineImage):
    page = ParentalKey(GalleryPage, on_delete=models.CASCADE, related_name='photo_pages')


class AboutImage(InlineImage):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='personal_photo')


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
