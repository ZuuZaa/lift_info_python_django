from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=200, verbose_name = 'xəbər başlığı')
    content = models.TextField(verbose_name = 'xəbərin mətni')
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True, verbose_name = 'tarix')

    class Meta:
        verbose_name = 'Xəbər'
        verbose_name_plural = 'Xəbərlər'

    def save(self):
        super(News, self).save()
        string_slug = self.title + '-' + str(self.published.strftime('-%d-%m-%Y-%M'))
        self.slug = slugify(string_slug)
        super(News, self).save()

    def __str__(self):
        return self.title

    
class Images(models.Model):

    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name = 'xəbər')
    img = models.ImageField(upload_to='news/',  verbose_name = 'şəkil')

    class Meta:
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'

    def foto(self):
        if self.img:
            return mark_safe(f"<img src='{self.img.url}' style='width: 50px;'>")

    def image_for_template(self):
        if self.img:
            return mark_safe(f"<img src='{self.img.url}'>")