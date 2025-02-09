from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Investment
from .serializer import InvestmentSerializer

@api_view(['GET'])
def get_investments(request):
    """
    Fetch all investments or filter by 'ville' and 'etatAvancement'
    """
    ville = request.GET.get('ville', None)
    etat_avancement = request.GET.get('etatAvancement', None)

    # Fetch all investments
    investments = Investment.objects.all()

    # Apply filters if provided
    if ville:
        investments = investments.filter(ville__icontains=ville)

    if etat_avancement:
        investments = investments.filter(etatAvancement__icontains=etat_avancement)

    serializer = InvestmentSerializer(investments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_investment(request):
    """
    Create new investment
    """
    serializer = InvestmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def investment_detail(request, pk):
    """
    Select one particular investment by its primary key id.
    According to request method:
    "get" - fetch the investment's data
    "gut" - update the investment's data
    "patch" - update only the part of the investment's data
    "delete" - delete the investment's data
    """
    try:
        investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvestmentSerializer(investment)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InvestmentSerializer(investment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = InvestmentSerializer(investment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






