from django.db import models
from django.utils.text import slugify


class SiteEssentials(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.CharField(max_length=255, blank=True)
    cta = models.CharField("Call to Action", max_length=255, blank=True)

    def __str__(self):
        return self.headline


class Location(models.Model):
    CITY = "city"
    AREA = "area"

    LOCATION_TYPES = [
        (CITY, "City"),
        (AREA, "Area"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPES, default=AREA)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["parent", "slug"],
                name="unique_mandm_location_slug_per_parent",
            )
        ]
        indexes = [
            models.Index(fields=["parent", "slug"]),
            models.Index(fields=["is_active", "is_featured"]),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def full_slug(self):
        if self.parent:
            return f"{self.parent.full_slug}/{self.slug}"
        return self.slug

    @property
    def seo_path(self):
        return f"/service-areas/{self.full_slug}/"
