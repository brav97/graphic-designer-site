from django.db import models
from django.db import migrations, models


class IMAGES(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='GLEEAPP/images/')
    attachment = models.FileField(upload_to='GLEEAPP/attachments/', blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMAGES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('feature_image', models.ImageField(upload_to='GLEEAPP/images/')),
                ('attachment', models.FileField(upload_to='GLEEAPP/attachments/')),
            ],
        ),
    ]
