from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView feature"""
        an_apiview= [
            'uses HTTP methods as function (get,post,patch,put etc...)',
            'Is similar to a traditonal Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'hello!', 'an_apiview':an_apiview})