from datetime import date
from email.policy import default
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})


class Role(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("role", kwargs={"role_slug": self.slug})


class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date_started = models.DateField(default=date.today)
    date_released = models.DateField(default=date.today)
    repo_link = models.URLField(max_length=300)
    link = models.URLField(max_length=300, blank=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(3, message="Минимум 5 символов"),
            MaxLengthValidator(200, message="Максимум 200 символов"),
        ],
    )
    photo = models.ImageField(
        upload_to="photos/",
        default=None,
        blank=True,
        null=True,
        verbose_name="фото",
    )
    is_released = models.BooleanField(default=False)
    role = models.ForeignKey(
        Role, on_delete=models.PROTECT, related_name="projects", null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("project", kwargs={"project_slug": self.slug})
