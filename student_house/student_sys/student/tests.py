from django.test import TestCase, Client
from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='3333',
            phone='32232323',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='2323',
            phone='12123123123',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容与展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='232323',
            phone='23232323',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个{}的记录'.format(name))

    # 视图测试
    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='2323@dd.com',
            profession='程序员',
            qq='42323',
            phone='232312',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertEqual(b'test_for_post' in response.content, "response content msut contain 'test_for_post' ")
