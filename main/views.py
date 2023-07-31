from .serializer import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, DestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


def pagination_json(page, query, serializer, number_of_object):
    if page is None:
        page = 1
    p = Paginator(query, number_of_object)
    pg = p.page(page)
    ser = serializer(pg.object_list, many=True)

    if pg.has_next():
        next_page = pg.next_page_number()
    else:
        next_page = None

    if pg.has_previous():
        previous_page = pg.previous_page_number()
    else:
        previous_page = None

    pagination = {
        "next_page": next_page,
        "current_page": page,
        "previous_page": previous_page,
        "pages_count": p.num_pages,
        "number_of_object": number_of_object,
        "items_count": query.count()
    }
    dt = {
        "pagination": pagination,
        "result": ser.data
    }
    return dt


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(['POST'])
def Login(request):
    try:
        username = request.data("username")
        password = request.data("password")
        try:
            users = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user is not None:
               status = 200
               token, created = Token.objects.get_or_create(user=user)
               data = {
                   "status": status,
                   "username": username,
                   "user_id": users.id,
                   "token": token.key,
               }
            else:
                status = 403
                message = "Username yoki parol xato!"
                data = {
                        "status": status,
                        "message": message,
                    }
        except User.DoesNotExist:
            status = 404
            message = "Bunday foydalanuvchi mavjud emas!"
            data = {
                "status": status,
                "message": message,
            }
        return Response(data)
    except Exception as err:
        return Response({"error": f"{err}"})



# @api_view(['GET'])
# @authentication_classes([ BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)


class SliderView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class InformationView(ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IsPopularView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request):
        popular = self.queryset.filter(is_popular=True).all().order_by("-id")[:4]
        data = ProductsSerializer(popular, many=True).data
        return Response(data)


class AboutView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class WhyChooseOptionsView(ListAPIView):
    queryset = WhyChooseOptions.objects.all()
    serializer_class = WhyChooseOptionsSerializer


class WhyChooseView(ListAPIView):
    queryset = WhyChoose.objects.all()
    serializer_class = WhyChooseSerializer


class ProductsView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = LargeResultsSetPagination


class ClientFeedbackView(ListAPIView):
    queryset = ClientFeedback.objects.all()
    serializer_class = ClientFeedbackSerializer


class GalleryView(ListAPIView):
    queryset = OurGallery.objects.all()
    serializer_class = OurGallerySerializer

    def list(self, request):
        category = request.GET.get('ourgallerycategory')
        order = self.queryset.filter(by_category=category)
        data = OurGallerySerializer(order, many=True).data
        return Response(data)


class GetNumberAreaView(ListAPIView):
    queryset = GetNumberArea.objects.all()
    serializer_class = GetNumberAreaSerializer


class LogoView(ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    def list(self, request):
        ser = LogoSerializer(self.get_queryset(), many=True).data
        return Response(ser)


class FaqView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def list(self, request):
        faqs = self.queryset.all().order_by('-id')[:5]
        return Response(self.serializer_class(faqs, many=True).data)


class FaqPhotoView(ListAPIView):
    queryset = FaqPhoto.objects.all()
    serializer_class = FaqSerializer

    def list(self, request):
        data = FaqSerializer(self.queryset, many=True).data
        return Response(data)


class ContactView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request):
        data = ContactSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"success": True})
        else:
            return Response({"success": False})


class BgImageView(ListAPIView):
    queryset = BgImage.objects.all()
    serializer_class = BgImageSerializer


class BlogAll(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        data = BlogSerializer(self.queryset, many=True).data
        return Response(data)


class BlogView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        blog = self.queryset.get(id=pk)
        comment = Comment.objects.filter(comment_blog=blog)
        comments = []
        for i in comment:
            comments.append(i.text)
            data = {
                "blog": BlogSerializer(blog).data,
                "comments": len(comments),
                "comment": CommentSerializer(comment, many=True).data
            }
        return Response(data)


class Blogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        data = self.queryset.all().order_by('-id')[:3]
        return Response(data)


class CommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ContactSerializer

    def create(self, request):
        text = request.POST.get("text")
        comment_blog = request.POST.get("comment_blog")
        ab_s = Blog.objects.get(id=comment_blog)
        b = Comment.objects.create(text=text, comment_blog=ab_s)
        return Response(CommentSerializer(b).data)


class LikeAdd(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        blog = self.queryset.get(id=pk)
        blog.like += 1
        blog.save()
        return Response(self.serializer_class(blog).data)


class LikeRemove(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        blog = self.queryset.get(id=pk)
        blog.like -= 1
        blog.save()
        return Response(self.serializer_class(blog).data)


class NewView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def list(self, request):
        last = self.queryset.all().order_by("-id")[:3]
        data = NewSerializer(last, many=True).data
        return Response(data)


class SubscribeView(CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def create(self, request):
        subs = SubscribeSerializer(data=request.data)
        if subs.is_valid():
            subs.save()
            return Response({"message": "Done"})
        else:
            return Response({"message": False})


class RecentProductView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request):
        product = self.queryset.all().order_by('-id')[:3]
        data = self.serializer_class(product, many=True).data
        return Response(data)


class AddCartView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def create(self, request, pk):
        try:
            product = self.queryset.get(id=pk)
            price = product.price
            Card.objects.create(
                user=request.user,
                product=product,
                price=price,
            )
            return Response({"success": True})
        except Exception as err:
            return Response({"error": f"{err}"})


class DeleteCardView(DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        cart = Card.objects.filter(user=request.user)
        if cart.user == request.user:
            self.queryset.get(id=pk).delete()
        return Response({"message": "Done"})


class GetCartView(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request):
        data = CardSerializer(self.queryset, many=True).data
        return Response(data)

class AddWishlist(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, pk):
        try:
            product = self.queryset.get(id=pk)
            price = product.price
            Wishlist.objects.create(
                user=request.user,
                product=product,
                price=price,
            )
            return Response({'success': True})
        except Exception as err:
            return Response({"error": f"{err}"})


class DeleteWishlist(DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        wish = Wishlist.objects.filter(user=request.user)
        if wish.user == request.user:
            self.queryset.get(id=pk)
        return Response({"message": "Done"})


class Search(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def search(self, request):
        search = request.GET.get('search')
        products = self.queryset.filter(name__icontains=search)
        return Response(ProductsSerializer(products, many=True).data)


from datetime import datetime


@api_view(['POST'])
@authentication_classes([ TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    card = Card.objects.filter(user=user)
    order = Order.objects.create(user=user, date=datetime.now().date(), total=0, address=request.POST.get("address"))
    total = 0
    for i in card:
        OrderItem.objects.create(
             order=order,
             product=i.product,
             quantity=i.quantity,
             price=i.product.price,
         )
        total += i.quantity *i.product.price
    order.total += total
    order.save()
    card.delete()
    return Response({"success": True})





















