from django.core.management.base import BaseCommand
from Menu.models import Catagory

class Command(BaseCommand):

    def handle(self, *args, **options):
        Catagory.objects.all().delete()

        categories = [
    "Tiffin Items",
    "Rice Varieties",
    "Snacks",
    "Beverages",
    "Biryani",
    "Parotta",
    "Fast Food",
    "Sweets and Desserts"
]
        descriptions = [
    "Traditional South Indian breakfast dishes like Idli, Dosa, and Pongal, perfect for a quick, healthy start to the day.",
    "A variety of flavorful rice-based dishes such as Sambar Rice, Lemon Rice, and Fried Rice, popular for lunch.",
    "Crispy and delicious quick bites like Bajji, Samosa, and French Fries, ideal for snack breaks.",
    "Refreshing hot and cold beverages including Filter Coffee, Tea, Jigarthanda, and Milkshakes.",
    "Fragrant and hearty biryanis like Chicken Biryani, Mutton Biryani, and Egg Biryani, loved by everyone.",
    "Soft and flaky Parottas and spicy Kothu Parottas, a staple in Tamil Nadu street food.",
    "A mix of international fast food options like Burgers, Sandwiches, Rolls, and Pasta, catering to modern tastes.",
    "Sweet treats and desserts such as Gulab Jamun, Ice Cream, and Payasam, perfect for satisfying a sweet tooth."
]

        for name,desc in zip(categories,descriptions):
            Catagory.objects.create(name=name,description=desc)