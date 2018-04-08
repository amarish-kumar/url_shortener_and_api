from rest_framework.serializers import ModelSerializer

from shortener.models import bitlyURL


class URLSerializer(ModelSerializer):
    class Meta:
        model = bitlyURL
        fields = [
            "url",
            "shortcode",
            "count",
            "short_url"
        ]