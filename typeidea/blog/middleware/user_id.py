import uuid

USER_KEY = 'uid'
TEN_YEARS = 60*60*24*365*10


class UserIDMiddleware:
    # 通过Middleware中间层来截取客户端每次访问和返回信息流，进行处理。
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 给客户端的request对象增加uid属性
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        # 在客户端Cookie中设置uid
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        # 生成用户唯一标识uid
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
