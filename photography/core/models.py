from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    fivehundredpx = models.URLField(
        help_text="Your 500px page URL",
        blank=True
    )
    facebook = models.URLField(
        help_text="Your Facebook page URL",
        blank = True
    )
    instagram = models.URLField(
        help_text="Your Instagram page URL",
        blank=True
    )