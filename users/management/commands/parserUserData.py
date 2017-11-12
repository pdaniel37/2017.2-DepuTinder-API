from users.models import Users
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def oneUser(self):
        user = User.objects.create_user('calebe', 'c@c.com', 'calebe')
        user.save()

    def parseData(self):
        for i in range(10):
            user, created = User.objects.get_or_create(
                username = fake.name(),
                password = fake.password(),
                email = fake.email(),
            )

            users, created2 = Users.objects.get_or_create(
                user = user,
                userImage = fake.text(),
            )

            if created and created2:
                self.stdout.write("Usuário " + users.user.username + " salvo com sucesso!")
            else:
                self.stdout.write("Usuário " + users.user.username + " não foi salvo no banco de dados!")
