import json
from json.decoder import JSONDecodeError

from django.views import View
from django.http  import JsonResponse

from .messages      import (
    MESSAGE_INVALID_JSON_FORMAT,
    MESSAGE_INVALID_SEARCH_TERM,
    MESSAGE_INVALID_PRODUCT_ID,
    MESSAGE_KEY_ERROR
)
from .make_jsons    import (
    make_result_message_json,
    make_product_search_results_for_sell_json,
    make_product_detail_for_buy_and_sell_json,
)
from product.models import (
    Product,
    ProductSize,
)

class SearchProductForSellView(View):
    def post(self, request):
        DEFAULT_LIMIT = 20
        return JsonResponse({'message':'Search Product For Sell View POST'}, status = 200)

class ProductDetailForBuyAndSellView(View):
    def post(self, request):
        return JsonResponse({'message':'Product Detail For Buy And Sell View POST', status = 200)
