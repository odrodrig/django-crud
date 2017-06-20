from django.test import TestCase
from postgresqlCRUD.models import People

class PeopleTest(TestCase):

    def test_str(self):

        person = People(first_name='John', last_name='Smith')

        self.assertEquals(
            str(person),
            'John Smith'
        )

# Create your tests here.
