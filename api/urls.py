from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import viewsets
from .boards.views import BoardViewSet
# from .lists.views import ListViewSet
# from .cards.views import CardViewSet
# from .comments.views import CommentViewSet
# from .attachments.views import AttachmentViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
# router.register(r'lists', ListViewSet)
# router.register(r'cards', CardViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'attachments', AttachmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
