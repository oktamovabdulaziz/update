from django.urls import path
from .views import *


urlpatterns = [
    path("slider/", SliderView.as_view()),
    path("category/", CategoryView.as_view()),
    path("is-popular/", IsPopularView.as_view()),
    path("about/", AboutView.as_view()),
    path("why-choose-options/", WhyChooseOptionsView.as_view()),
    path("why-choose/", WhyChooseView.as_view()),
    path("products/", ProductsView.as_view()),
    path("client-feedback/", ClientFeedbackView.as_view()),
    path("gallery/", GalleryView.as_view()),
    path("logo/", LogoView.as_view()),
    path("contact/", ContactView.as_view()),
    path("get-number-area/", GetNumberAreaView.as_view()),
    path("bg-image/", BgImageView.as_view()),
    path("blog/", BlogView.as_view()),
    path("blog-all/", BlogAll.as_view()),
    path("new/", NewView.as_view()),
    path("information/", InformationView.as_view()),
    path("comment/", CommentView.as_view()),
    path("like-add/<int:pk>/", LikeAdd.as_view()),
    path("like-remove/<int:pk>/", LikeRemove.as_view()),
    path("faq/", FaqView.as_view()),
    path("recent-product/", RecentProductView.as_view()),
    path("subscribe/", SubscribeView.as_view()),
    path("add-cart/<int:pk>/", AddCartView.as_view()),
    path("delete-card/<int:pk>/", DeleteCardView.as_view()),
    path("add-wishlist/<int:pk>/", AddWishlist.as_view()),
    path("delete-wishlist/<int:pk>/", DeleteWishlist.as_view()),
    path("search/", Search.as_view()),
    path("create-order/", create_order),
]


