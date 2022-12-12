from django.urls import reverse,include,path
from recipe.views import RecipeViewSet , TagViewSet,IngredientListView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientListView)
app_name='recipe'

urlpatterns=[
    path('' , include(router.urls)),
]