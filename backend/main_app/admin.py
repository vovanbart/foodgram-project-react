from django.contrib.admin import ModelAdmin, TabularInline, register
from django.contrib import admin

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
    list_filter = ('measurement_unit')


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    inlines = [IngredientInline]
    list_display = ('name', 'author')
    list_filter = ('tags',)
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


class CartAdmin(ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__username',)
    list_filter = ('recipe__tags__name',)


admin.site.register(Cart, CartAdmin)
