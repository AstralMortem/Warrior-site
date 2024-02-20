from .base import *
DEBUG=False



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
    "staticfiles": 
        {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
        }
}

CSRF_TRUSTED_ORIGINS = [
    'https://api.warrior-tkd.pp.ua'
]