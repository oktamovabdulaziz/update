from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=255)


class Slider(models.Model):
    photo = models.ImageField(upload_to='slider/')
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()
    img_text = models.TextField()
    video = models.FileField()
    bg_img = models.ImageField()

    def __str__(self):
        return self.title


class GetNumberArea(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    numbers = models.IntegerField()

    def __str__(self):
        return self.name


class WhyChooseOptions(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WhyChoose(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    options = models.ManyToManyField(WhyChooseOptions)
    photo = models.ImageField(upload_to="choose/")

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    price = models.IntegerField()
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ClientFeedback(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='Client/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OurGalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OurGallery(models.Model):
    img = models.ImageField()
    by_category = models.ForeignKey(OurGalleryCategory, on_delete=models.CASCADE)


class Logo(models.Model):
    logo = models.ImageField(upload_to='Logo/')


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    logo = models.ImageField(upload_to='Info/')
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    fb = models.URLField()
    ins = models.URLField()
    tw = models.URLField()
    yt = models.URLField()
    map = models.CharField(max_length=255)


class Subscribe(models.Model):
    email = models.EmailField()


class BgImage(models.Model):
    bg_img = models.ImageField()


class Blog(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=255)
    comment_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class New(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class FaqPhoto(models.Model):
    photo = models.ImageField(upload_to='faqs/')


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()



# 1. is_popular product ni fieldi boladi wundan filtr qilib olish kerak /
# 2. get numbers area /
# 3.  add wishlist /
# 4.  delete cart tekwirish kerak /
# 5. delete wishlist /
# 6. edit cart
# 7. our gallary (by_category) /
# 8. news get last 3  /
# 9. subscribe post /
# 10. blog all get /
# 11. product single get /


# 12. cart get
