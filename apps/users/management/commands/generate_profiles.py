import random
from pathlib import Path
from typing import Any

import names
from django.core.files import File
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.utils import lorem_ipsum
from django.utils.text import slugify

from users.models import Profile, User

IMG_PATH = Path(__file__).parent / "images"


class Command(BaseCommand):
    """Generate Random Profiles."""

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("-n", "--number", default=5, type=int)

    def handle(self, **options: Any) -> None:
        all_images = list(IMG_PATH.glob("*.jpg"))

        for _ in range(options["number"]):
            f_name = names.get_first_name()
            l_name = names.get_last_name()

            f_slug = slugify(f_name)
            l_slug = slugify(l_name)

            user = User.objects.create_user(
                email=f"{f_slug}@{l_slug}.com",
                password="password",
                first_name=f_name,
                last_name=l_name,
            )

            sentences = (lorem_ipsum.sentence(), lorem_ipsum.sentence())
            profile = Profile.objects.create(
                user=user,
                bio="\n\n".join(sentences),
            )

            rnd_img = random.choice(all_images)
            content = File(rnd_img.open("rb"))
            profile.avatar.save(f"{f_slug}_{l_slug}.jpg", content)
