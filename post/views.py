# from django.db.models import Count
# from django.db.models.functions import TruncDate
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import (
    PostSerializer,
    LikeActionSerializer,
    # AnalyticsSerializer,
    CreatePostSerializer
)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePostSerializer
        return PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(APIView):
    serializer_class = LikeActionSerializer

    def post(self, request, pk):
        user = request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Пост не існує."}, status=status.HTTP_404_NOT_FOUND
            )

        if post.likes.filter(id=user.id).exists():
            return Response(
                {"detail": "Ви вже лайкнули цей пост."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        post.likes.add(user)
        post.save()
        return Response(
            {"detail": "Пост був лайкнутий успішно."},
            status=status.HTTP_201_CREATED
        )


class UnlikePostView(APIView):
    serializer_class = LikeActionSerializer

    def post(self, request, pk):
        user = request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Пост не існує."}, status=status.HTTP_404_NOT_FOUND
            )

        if not post.likes.filter(id=user.id).exists():
            return Response(
                {
                    "detail":
                        "Ви не лайкнули цей пост, тому не можете дизлайкнути."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        post.likes.remove(user)
        post.save()
        return Response(
            {"detail": "Пост був дизлайкнутий успішно."},
            status=status.HTTP_204_NO_CONTENT,
        )


# class AnalyticsView(generics.ListAPIView):
#     serializer_class = AnalyticsSerializer
#
#     def get_queryset(self):
#         date_from = self.request.query_params.get("date_from")
#         date_to = self.request.query_params.get("date_to")
#
#         queryset = Post.objects.all()
#
#         if date_from and date_to:
#             queryset = queryset.filter(
#                 created_at__date__range=[date_from, date_to]
#             )
#
#         queryset = (
#             queryset.annotate(date=TruncDate("created_at"))
#             .values("date")
#             .annotate(count=Count("likes"))
#             .order_by("date")
#         )
#         return queryset
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
