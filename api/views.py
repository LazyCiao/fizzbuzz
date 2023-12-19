from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FizzBuzzView(APIView):
    def get(self, request, format=None):
        # Retrieve parameters from the request
        int1 = request.query_params.get('int1')
        int2 = request.query_params.get('int2')
        limit = request.query_params.get('limit')
        str1 = request.query_params.get('str1')
        str2 = request.query_params.get('str2')

        # Check if all parameters are provided
        if not all([int1, int2, limit, str1, str2]):
            return Response({"error": "All parameters (int1, int2, limit, str1, str2) are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Convert string parameters to integers and validate
        try:
            int1 = int(int1)
            int2 = int(int2)
            limit = int(limit)
        except ValueError:
            return Response({"error": "Invalid input, integers expected for int1, int2, and limit."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Fizz-Buzz logic
        result = []
        for i in range(1, limit + 1):
            if i % int1 == 0 and i % int2 == 0:
                result.append(str1 + str2)
            elif i % int1 == 0:
                result.append(str1)
            elif i % int2 == 0:
                result.append(str2)
            else:
                result.append(str(i))

        return Response(result)