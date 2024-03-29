import shortuuid

from source.ports.url_repository import UrlRepository

class ShortUUIDGenerator():
    url_repo: UrlRepository

    def generate_key(self, length=8) -> str:
        """this generator will create a short uuid"""
        return shortuuid.ShortUUID().random(length=length)
