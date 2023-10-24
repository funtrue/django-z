import logging


LOGGER = logging.getLogger("middleware_log")

class IP_delete_can:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(request.META['REMOTE_ADDR'], request.path, request.user.is_superuser)
        LOGGER.info("自定义中间件：访问本服务IP为 %s" % request.META['REMOTE_ADDR'])
        # if (request.user.is_superuser != True) and (request.path == '/'):
        #     return HttpResponseForbidden('<h1>超级用户方可访问此页面！</h1>')

        response = self.get_response(request)

        return response