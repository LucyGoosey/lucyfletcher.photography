from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = "Social Media Accounts"

    def fivehundredpx(self):
        return self._500px

    def fivehundredpx_text(self):
        return self._500px_Text

    _500px = models.URLField(
        help_text="Your 500px page URL",
        blank=True
    )
    _500px_Text = models.TextField(
        help_text="If set this text will show instead of the Font Awesome logo",
        blank=True
    )

    facebook = models.URLField(
        help_text="Your Facebook page URL",
        blank=True
    )
    facebook_Text = models.TextField(
        help_text="If set this text will show instead of the Font Awesome logo",
        blank=True
    )

    instagram = models.URLField(
        help_text="Your Instagram page URL",
        blank=True
    )
    instagram_Text = models.TextField(
        help_text="If set this text will show instead of the Font Awesome logo",
        blank=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('_500px'),
                FieldPanel('_500px_Text')
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('facebook_Text')
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel('instagram'),
                FieldPanel('instagram_Text')
            ]
        ),
    ]