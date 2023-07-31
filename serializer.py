from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class WhyChooseOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseOptions
        fields = "__all__"


class WhyChooseSerializer(serializers.ModelSerializer):
    options = WhyChooseOptionsSerializer(many=True)

    class Meta:
        model = WhyChoose
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = "__all__"


class OurGalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGalleryCategory
        fields = "__all__"


class OurGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGallery
        fields = "__all__"


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class GetNumberAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetNumberArea
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"


class BgImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BgImage
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class FaqPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqPhoto
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


