from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from core.models import Profile
from portal.views import home, ticket, dashboard, create_ticket, issue_search
from django.contrib import admin


class ProfileModelTest(TestCase):

    def setUp(self):
        random_password = User.objects.make_random_password()
        self.user1 = User.objects.create_user(username='testuser1', password=random_password)
        self.user2 = User.objects.create_user(username='testuser2', password=random_password, email='testuser2@example.com')
        self.profile1 = Profile.objects.get(user=self.user1)
        self.profile2 = Profile.objects.get(user=self.user2)

    def test_profile_creation(self):
        self.assertIsNotNone(self.profile1)
        self.assertIsNotNone(self.profile2)

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile1), 'testuser1')
        self.assertEqual(str(self.profile2), 'testuser2')

    def test_profile_default_role(self):
        self.assertEqual(self.profile1.role, Profile.Role.user_role)
        self.assertEqual(self.profile2.role, Profile.Role.user_role)

    def test_role_choices(self):
        self.profile1.role = Profile.Role.agent_role
        self.profile1.save()
        self.profile2.role = Profile.Role.admin_role
        self.profile2.save()

        self.assertEqual(self.profile1.role, Profile.Role.agent_role)
        self.assertEqual(self.profile2.role, Profile.Role.admin_role)

    def test_create_or_update_user_profile(self):
        user3 = User.objects.create_user(username='testuser3', password=random_password)
        profile3 = Profile.objects.get(user=user3)
        self.assertIsNotNone(profile3)

    def test_save_user_profile(self):
        self.profile1.role = Profile.Role.agent_role
        self.profile1.user.save()
        updated_profile = Profile.objects.get(user=self.user1)
        self.assertEqual(updated_profile.role, Profile.Role.agent_role)
