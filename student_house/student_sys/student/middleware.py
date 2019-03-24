import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# 这是一个接口，继承了MiddlewareMixin接口后，
# 可以对每一次request请求进行处理
class TimeItMiddleware(MiddlewareMixin):
    # 当一个request请求进来以后，第一个执行的方法
    # 可以在这里进行身份校验或者HTTP头部校验
    def process_request(self, request):
        self.start_time = time.time()
        return None

    # 当process_request返回None时执行
    # 这里我们模拟需要测量视图函数执行时间
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(request)   # Func 是一个视图函数
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response

    # 当Process_view中视图函数调用发生异常，或页面渲染出现异常时调用
    def process_exception(self, request, exception):
        # 可以自行处理异常然后返回 HttpResponse
        # 也可以不处理返回 None，由 Django 自己处理
        pass

    # 成功执行了上述函数后，如果使用了模版，就会进入这个方法
    # 如：render(request, 'index.html', context={})
    def process_template_response(self, request, response):
        return response

    # 最后执行的方法，和process_template_response类似，
    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request to response cose: {:.2f}s'.format(costed))
        return response
