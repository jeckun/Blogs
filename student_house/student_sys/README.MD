# 第一个系统：学员管理系统

这个系统主要应用场景是学员在线注册，后台管理老师进行审批。并且前端可以查看哪些学员以及注册成功。

应用效果如下：前端界面

![前端](https://github.com/jeckun/Django_test/blob/master/student_house/student_sys/student/image/stu_index.png)

应用效果如下：管理界面


![后端](https://github.com/jeckun/Django_test/blob/master/student_house/student_sys/student/image/stu_admin.png)

## 创建学员管理系统站点

```
$ mkdir student_house
$ cd student_house && django-admin startproject student_sys
$ cd student_house/student_sys
$ python manage.py startapp student

```

