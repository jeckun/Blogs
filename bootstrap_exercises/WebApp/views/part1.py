from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json


def bootstrap(request, **kwargs):
  return render(request, "bootstrap.html", context=None)


def bootstrap_table(request, **kwargs):
  return render(request, "bootstrap_table.html", context=None)


def response(*args, **kwargs):
    """
    从服务端作出响应，返回任意值。
    既可以是一个字符串，也可以是一段HTML代码。
    :param args:
    :param kwargs:
    :return:
    """
    content = "<h1>Hellow world.</h1>"
    return HttpResponse(content, *args, **kwargs)


def get_json(request, **kwargs):
    data = {
      "total": 11,
      "rows":[
      {
        'id': 0,
        'name': 'Item 0',
        'price': '$0'
      },
      {
        'id': 1,
        'name': 'Item 2',
        'price': '$15'
      },
      {
        'id': 2,
        'name': 'Item 3',
        'price': '$25'
      },
      {
        'id': 3,
        'name': 'Item 4',
        'price': '$25'
      },
      {
        'id': 4,
        'name': 'Item 5',
        'price': '$25'
      },
      {
        'id': 5,
        'name': 'Item 6',
        'price': '$25'
      },
      {
        'id': 6,
        'name': 'Item 7',
        'price': '$25'
      },
      {
        'id': 7,
        'name': 'Item 8',
        'price': '$25'
      },
      {
        'id': 8,
        'name': 'Item 9',
        'price': '$25'
      },
      {
        'id': 9,
        'name': 'Item 10',
        'price': '$25'
      },
      {
        'id': 10,
        'name': 'Item 11',
        'price': '$25'
      }]
    }
    return HttpResponse(json.dumps(data))