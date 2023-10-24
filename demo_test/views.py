from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class DemoGet(GenericAPIView):
    # queryset = Virtual_machine.objects.all()
    # serializer_class = VMSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # filterset_fields = ['vm_ip',]
    
    def get(self, request):
        """
        虚拟机信息获取接口
        """
        # query_set = self.get_queryset()
        # qs = self.filter_queryset(query_set)
        # serializer = self.get_serializer(qs, many=True)
        dct = {
            "nihao": 123
        }
        return Response(dct)
