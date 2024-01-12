from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is manually mapped to URLs'
        ]

        return Response(
            {
                'message' : 'Hello!',
                'an_apiview' : an_apiview,
            }
        )
