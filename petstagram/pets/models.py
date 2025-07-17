from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.db import models

UserModel = get_user_model()

class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )
    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        blank=True,
        null=False,
        unique=True,
        editable=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
