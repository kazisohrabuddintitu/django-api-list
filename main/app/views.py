from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import get_resolver

class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        url_resolver = get_resolver()
        api_urls = []

        for url_pattern in url_resolver.url_patterns:
            if hasattr(url_pattern, 'pattern'):
                pattern = url_pattern.pattern
                if isinstance(pattern, str) and 'api' in pattern:
                    api_urls.append(request.build_absolute_uri(pattern))

        return Response(api_urls)