from django.contrib.auth import get_user_model
from journies import models
from graphene_django import DjangoObjectType
import graphene

class userType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class userProfileType(DjangoObjectType):
    class Meta:
        model = models.userProfile

class tagType(DjangoObjectType):
    class Meta:
        model = models.tag

class postType(DjangoObjectType):
    class Meta:
        model = models.post


class Query(graphene.ObjectType):

    all_posts = graphene.List(postType)
    author_by_username = graphene.Field(userProfileType, username = graphene.String())
    post_by_slug = graphene.Field(postType, slug = graphene.String())
    post_by_author = graphene.List(postType, username = graphene.String())
    post_by_tag = graphene.List(postType, tag = graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.post.objects
            .prefetch_related("tags")
            .select_related("author")
        )

    def resolve_author_by_username(root, info, username):
        return (
            models.userProfile.objects
            .select_related("user")
            .get(user__username=username)
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.post.objects
            .prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_post_by_author(root, info, username):
        return (
            models.post.objects
            .prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_post_by_tag(root, info, tag):
        return (
            models.post.objects.
            prefetch_related("tags")
            .select_related("author")
            .filter(tags__name=tag)
        )

schema = graphene.Schema(query=Query)