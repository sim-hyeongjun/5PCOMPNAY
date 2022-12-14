from django.contrib import admin
# models에서 BlogData를 import 해옵니다.
from parsed_data.models import BlogData
from deal.models import deal
from auction.models import auctionData
from charter.models import charterData
# 아래의 코드를 입력하면 BlogData를 admin 페이지에서 관리할 수 있습니다.
admin.site.register(BlogData)
admin.site.register(deal)
admin.site.register(auctionData)
admin.site.register(charterData)