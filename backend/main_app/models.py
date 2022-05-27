from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=200, unique=True)
    color = models.CharField(
        verbose_name='Цвет в HEX', max_length=7, unique=True)
    slug = models.SlugField(
        verbose_name='Уникальный slug', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название', help_text='Введите название', max_length=200)
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=20,
        help_text='Введите единицу измерения')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('name',)
        constraints = (
            models.UniqueConstraint(fields=('name', 'measurement_unit',),
                                    name='unique_for_ingredient'),)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор публикации',
        related_name='recipes',
        help_text='Введите автора',
    )
    name = models.CharField(
        verbose_name='Название', help_text='Введите название', max_length=200)
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Вставьте картинку',
        upload_to='recipe_images/')
    text = models.TextField(
        verbose_name='Текстовое описание',
        help_text='Введите текстовое описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='main_app.IngredientAmount',
        verbose_name='Ингредиенты',
        help_text='Введите ингредиенты',
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        help_text='Введите тэг',
        related_name='recipes')
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        help_text='Введите время приготовления',
        validators=(validators.MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),
        )
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )

    def __str__(self) -> str:
        return self.name


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='В каких рецептах',
        help_text='Введите рецепты',
        related_name='ingredient',
    )
    ingredients = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Связанные ингредиенты',
        help_text='Введите ингредиенты',
        related_name='recipe',
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=(
            validators.MinValueValidator(
                1, message='Минимальное количество ингридиентов 1'),),
        verbose_name='Количество',
        help_text='Введите количество',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Количество ингридиента'
        verbose_name_plural = 'Количество ингридиентов'
        constraints = (
            models.UniqueConstraint(fields=['recipe', 'ingredients'],
                                    name='unique_ingredients_recipe'),
        )

    def __str__(self) -> str:
        return self.ingredients.name, '-', self.amount


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь',
        help_text='Введите пользователя',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Рецепт',
        help_text='Введите рецепт',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'В корзине'
        constraints = (
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_cart_user'),
        )

    def __str__(self) -> str:
        return f'У {self.user} в списке покупок {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Введите пользователя',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
        help_text='Введите рецепт',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = (
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_user_recipe'),
        )

    def __str__(self):
        return f'У {self.user} в избранном {self.recipe}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Введите пользователя',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Введите пользователя',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_follow',
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
