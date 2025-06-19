from django.test import TestCase
from data_entry.models import Pengguna

class PenggunaModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData dijalankan')
        Pengguna.objects.create(
            email='aku@gmail.com',
            address_1='Kampus A Usakti, Grogol',
            city='Jakarta',
            state='DKI Jakarta'
        )

    def test_email_label(self):
        print('test_email_label dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        field_label = pengguna._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_address_max_length(self):
        print('test_address_max_length dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        max_length = pengguna._meta.get_field('address_1').max_length
        self.assertEqual(max_length, 200)

    def test_object_str_is_email(self):
        print('test_object_str_is_email dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        expected_object_name = pengguna.email
        self.assertEqual(str(pengguna), expected_object_name)
