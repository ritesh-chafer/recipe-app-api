from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

RECIPES_URL = reverse("recipe:Recipe-list")


def sample_recipe(user, **params):
    """create and return a sample recipe"""
    defaults={
        'title' : 'Streak and mushroom sauce',
        'time_minutes':5,
        'price' : 5.00
    }

    defaults.update(params)

    return Recipe.objects.create(user = user, **defaults)

class PublicRecipeApiTests(TestCase):
    """Test the publicly available ingredients API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(RECIPES_URL)
 
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
