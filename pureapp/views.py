from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pureapp.models import Pure
from pureapp.serialzers import Student

# Create your views here.
@api_view(['GET'])
def home(request):
    odata=Pure.objects.all()
    serail=Student(odata,many=True)

    return Response({'status':200,'payload':serail.data})
    
@api_view(['POST'])
def homes(request):
    if request.method == 'POST':

        serail=Student(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response({'status':200,'messages':'done','payload':serail.data})

    else:
        odata=Pure.objects.all()
        serail=Student(odata,many=True)


    return Response({'status':200,'payload':serail.data,'message':'data is not saved'})
    

@api_view(['PUT'])
def homess(request,id):
    if request.method == 'PUT':
        d=Pure.objects.get(pk=id)
        serail=Student(d,data=request.data)
        if serail.is_valid():
            serail.save()
            return Response({'status':200,'messages':'done','payload':serail.data})

    else:
        odata=Pure.objects.all()
        serail=Student(odata,many=True)


    return Response({'status':200,'payload':serail.data,'message':'data is not saved'})
    


@api_view(['PATCH'])
def homesss(request,id):
    d=Pure.objects.get(pk=id)
    serail=Student(d,data=request.data,partial=True)
    if serail.is_valid():
        serail.save()
        return Response({'status':200,'messages':'done','payload':serail.data})
    else:
        return Response({'status':403,'messages':'not done'})


@api_view(['DELETE'])
def homessss(request,id):
    d=Pure.objects.get(pk=id)
    d.delete()
    
   
    return Response({'status':200,'messages':'done'})

   


  
    

