from django.core.management.base import BaseCommand
from Menu.models import Product,Catagory,NutritionalInfo

class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        # Lists for Tamil Nadu food items
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

        description = [
            "Steamed rice cake", "Crispy rice and lentil crepe", "Rice and moong dal porridge", 
            "Thick dosa with toppings", "Fried lentil doughnut",
            "Rice cooked with lentils and spices", "Rice mixed with yogurt", "Rice cooked with tomato and spices", 
            "Rice flavored with lemon and spices", "Rice cooked with grated coconut",
            "Crispy fried banana slices", "Crunchy rice flour snack", "Fried fritters with gram flour", 
            "Vegetable fritters", "Deep-fried rice flour balls",
            "South Indian coffee with milk", "Spiced tea with milk", "Cooling drink made with nannari syrup", 
            "Spiced yogurt drink", "Fresh coconut water",
            "Fragrant rice with chicken", "Fragrant rice with mutton", "Rice with mixed vegetables", 
            "Rice with prawns and spices", "Rice with boiled eggs",
            "Layered flatbread", "Parotta shredded and cooked with spices", "Parotta with egg", 
            "Parotta with chicken stuffing", "Parotta cooked with vegetables and spices",
            "Deep-fried chicken with spices", "Burger with vegetable patty", "Crispy fried potato sticks", 
            "Flatbread roll stuffed with paneer", "Middle Eastern-style chicken wrap",
            "Sweet made with ghee and gram flour", "Sweet deep-fried spirals soaked in sugar syrup", 
            "Semolina sweet flavored with saffron", "Milk and rice pudding", "Sweet dense pudding made with wheat"
        ]

        quantity = [
            2, 1, 1, 1, 2,
            1, 1, 1, 1, 1,
            100, 100, 100, 100, 100,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            2, 1, 1, 1, 1,
            1, 1, 100, 1, 1,
            100, 100, 1, 1, 100
        ]

        vegornonveg = [
            "Veg", "Veg", "Veg", "Veg", "Veg",
            "Veg", "Veg", "Veg", "Veg", "Veg",
            "Veg", "Veg", "Veg", "Veg", "Veg",
            "Veg", "Veg", "Veg", "Veg", "Veg",
            "Non-Veg", "Non-Veg", "Veg", "Non-Veg", "Non-Veg",
            "Veg", "Non-Veg", "Non-Veg", "Non-Veg", "Veg",
            "Non-Veg", "Veg", "Veg", "Veg", "Non-Veg",
            "Veg", "Veg", "Veg", "Veg", "Veg"
        ]

        actual_price = [
            40, 50, 60, 70, 40,
            80, 60, 70, 60, 70,
            50, 60, 60, 50, 60,
            30, 20, 40, 20, 50,
            150, 200, 120, 180, 130,
            40, 100, 60, 120, 90,
            100, 80, 50, 90, 120,
            80, 70, 60, 50, 90
        ]

        discount_price = [
            35, 45, 55, 65, 35,
            70, 50, 65, 55, 65,
            45, 50, 55, 45, 55,
            25, 15, 35, 15, 45,
            140, 190, 110, 170, 120,
            35, 90, 50, 110, 80,
            90, 70, 45, 80, 110,
            70, 60, 50, 45, 80
        ]
        ct,count = 0, 1
        for pro_name,pro_description,pro_quantity,vnv,ap,dp,ni in zip(name,description,quantity,vegornonveg,actual_price,discount_price,range(1,41)):
            cat_obj = Catagory.objects.get(pk=1 if ct==0 else ct+1)
            ni_obj = NutritionalInfo.objects.get(pk=ni)
            Product.objects.create(name=pro_name,description=pro_description,quantity=pro_quantity,label=vnv,actuall_price=ap,discount_price=dp,nutritionalinfo=ni_obj,catagory=cat_obj)
            
            if count%5==0:
                ct+=1
            count+=1
            print(ct,count,ni)