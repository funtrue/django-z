from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from demo_test.models import Demo_Model
from demo_test.serializer import DMSerializer
from demo_test.task import task_finish, demo_task
from django_q.tasks import async_task

class DemoGet(GenericAPIView):
    queryset = Demo_Model.objects.all()
    serializer_class = DMSerializer
    filterset_fields = ['demo_ip',]
    
    def get(self, request):
        """
        测试虚拟机信息获取接口
        """
        query_set = self.get_queryset()
        qs = self.filter_queryset(query_set)
        serializer = self.get_serializer(qs, many=True)
        
        # django-q异步任务事例
        # async_task(
        #     demo_task, 10,
        #     task_name='test',
        #     hook=task_finish,
        # )
        return Response(serializer.data)
