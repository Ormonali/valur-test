from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def calculate(request):
    first_value = request.data.get('first_value')
    second_value = request.data.get('second_value')
    
    if first_value is None or second_value is None:
        return Response({'error': 'Both first_value and second_value are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        result = int(first_value) * int(second_value)
        return Response({'result': result})
    except ValueError:
        return Response({'error': 'Invalid input. Both values must be integers'}, status=status.HTTP_400_BAD_REQUEST)
