import json, bcrypt, jwt, requests

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import Prefetch, Max, Min

from .models          import User, Follow
from product.models   import Product, ProductSize
from sale.models      import Status, Ask, UserAsk, Bid
from .utils           import login_required
from .validation      import ValidationError
from westock.settings import SECRET_KEY, ALGORITHM
from datetime         import datetime

class SignUp(View):
    def post(self, request):
        return JsonResponse({'message':'Sign Up View POST'}, status = 200)

class SignIn(View):
    def post(self, request):
        return JsonResponse({'message':'Sign In View'}, status = 200)

class KakaoSignin(View):
    def post(self, request):
        return JsonResponse({'message':'Kakao Sign In View'}, status = 200)

class GoogleSignInView(View):
    def get(self, request):
        return JsonResponse({'message': 'Google Sign In View'}, status = 200)

class ProductFollow(View):
    def post(self, request):
        data = json.loads(request.body)
        user = request.account

        Follow.objects.filter(user = user).delete()
        product_sizes = ProductSize.objects.filter(product_id = data['product'], size__name__in = data['sizes'])

        for product_size in product_sizes: Follow.objects.create(user = user, product_size = product_size)

        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)

class BuyingList(View):
    @login_required
    def get(self, request):
        user = request.account
        buying_infos = []
        buyings = user.bid_set.all()
        product_sizes = [buying.product_size for buying in buyings]
        for product_size in product_sizes:
            product_image = product_size.product.image_with_product.get(image_type__name = 'list').url
            expired_date = product_size.bid_set.get(user = user).expired_date
            product_info = {
                'product_size_id': product_size.id,
                'product_name':product_size.product.name,
                'product_style':product_size.product.style,
                'image_url': product_image,
                'expired_date': str(expired_date.date()),
                'price': product_size.bid_set.get(user = user).price
            }
            buying_info = product_size.ask_set.all().aggregate(lowest_ask = Min('price'))
            buying_info.update(product_size.bid_set.all().aggregate(highest_bid = Max('price')))
            buying_info.update(product_info)
            buying_infos.append(buying_info)

        return JsonResponse({'BUYING_INFOS':buying_infos}, status = 200)
