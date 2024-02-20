from .base import *

SECRET_KEY = "django-insecure-c&7m1%3(1(+kv3!sp%4)0fo)=6j26mj%^_1m_0=s*w%-&4plf5"
DEBUG=False

ALLOWED_HOSTS = ['*']



STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS":{
            "access_key": os.getenv("ACCESS_KEY"),
            "secret_key": os.getenv("SECRET_KEY"),
            "bucket_name": os.getenv("BUCKET_NAME"),
            "region_name": os.getenv("REGION_NAME"),
            "endpoint_url": f"https://{os.getenv('REGION_NAME')}.digitaloceanspaces.com",
            "object_parameters": {
                "CacheControl": "max-age=86400"
            },
            #"location": f"https://{os.getenv('BUCKET_NAME')}.{os.getenv('REGION_NAME')}.digitaloceanspaces.com"
        }
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    }
}

