from django.contrib.auth.models import AnonymousUser, User
from demo_test.models import Demo_Model
from django.test import RequestFactory, TestCase 
import os


class SimpleTest(TestCase):
    def setUp(self):
        Demo_Model.objects.create(
            demo_ip='127.1.1.1', demo_app_name='test', demo_status='NO',demo_describe="tests")
    
    def test_class_islife(self):
        ip_1 = Demo_Model.objects.get(demo_ip="127.1.1.1")
        # ip_2 = Demo_Model.objects.get(demo_ip="127.1.1.0")
        print(ip_1)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_z.settings")
    import django
    django.setup()
    