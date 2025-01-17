from django.core.management.base import BaseCommand
from Menu.models import NutritionalInfo

class Command(BaseCommand):
    NutritionalInfo.objects.all().delete()
    def handle(self, *args, **options):
         # Lists for Tamil Nadu food items with nutritional details
        name = [
            "Idli", "Dosa", "Pongal", "Uttapam", "Vada",
            "Sambar Rice", "Curd Rice", "Tomato Rice", "Lemon Rice", "Coconut Rice",
            "Banana Chips", "Murukku", "Pakoda", "Bhajji", "Seedai",
            "Filter Coffee", "Masala Chai", "Nannari Sherbet", "Butter Milk", "Tender Coconut Water",
            "Chicken Biryani", "Mutton Biryani", "Vegetable Biryani", "Prawn Biryani", "Egg Biryani",
            "Plain Parotta", "Kothu Parotta", "Egg Parotta", "Chicken Parotta", "Veg Kothu Parotta",
            "Chicken 65", "Veg Burger", "French Fries", "Paneer Roll", "Chicken Shawarma",
            "Mysore Pak", "Jangiri", "Rava Kesari", "Payasam", "Halwa"
        ]

        calories = [
            50, 120, 200, 150, 180,
            220, 180, 200, 190, 210,
            550, 450, 400, 300, 420,
            90, 100, 120, 50, 40,
            450, 500, 380, 420, 400,
            250, 400, 300, 400, 350,
            450, 320, 400, 380, 500,
            500, 450, 360, 300, 400
        ]

        carbs = [
            11, 25, 30, 20, 25,
            35, 30, 32, 31, 33,
            50, 40, 35, 28, 40,
            12, 15, 25, 5, 9,
            50, 55, 48, 50, 52,
            30, 40, 35, 45, 40,
            25, 40, 50, 45, 40,
            55, 48, 45, 40, 50
        ]

        proteins = [
            2, 4, 7, 5, 4,
            7, 5, 6, 5, 5,
            2, 5, 6, 3, 6,
            0, 1, 0, 1, 0,
            20, 25, 10, 22, 15,
            6, 12, 8, 15, 10,
            25, 10, 5, 12, 20,
            8, 6, 5, 5, 4
        ]

        fats = [
            0.5, 2, 6, 3, 10,
            5, 3, 4, 3, 5,
            35, 20, 25, 18, 25,
            3, 2, 0, 2, 0,
            15, 20, 8, 15, 10,
            8, 15, 10, 15, 12,
            30, 15, 20, 18, 25,
            25, 20, 15, 10, 20
        ]

        cholesterol = [
            0, 0, 5, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            50, 70, 10, 60, 40,
            0, 10, 20, 30, 5,
            80, 20, 0, 10, 60,
            10, 5, 0, 0, 0
        ]

        for n,cal,carb,por,fat,chols in zip(name,calories,carbs,proteins,fats,cholesterol):
            NutritionalInfo.objects.create(name=n,calories=cal,carbs=carb,proteins=por,fats=fat,cholesterol=chols)