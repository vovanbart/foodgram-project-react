from django.contrib.admin import ModelAdmin, TabularInline, register

from .models import (Cart,
                     Favorite,
                     Ingredient,
                     IngredientAmount,
                     Recipe,
                     Tag,
                     Follow, )


class IngredientInline(TabularInline):
    model = Recipe.ingredients.through


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'color')


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    inlines = [IngredientInline]
    list_display = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('count_favorites',)

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.short_description = 'Число добавлений в избранное'


@register(Follow)
class FollowAdmin(ModelAdmin):
    list_display = ('user', 'author')
    autocomplete_fields = ('author', 'user')
    search_fields = ('user', 'author',)


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    list_display = ('recipe', 'ingredients', 'amount',)
    search_fields = ('ingredients',)


@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('user', 'recipe')


@register(Cart)
class CartAdmin(ModelAdmin):
    list_display = ('user', 'recipe', 'get_tags',)

    def get_tags(self, obj):
        return obj.tags
