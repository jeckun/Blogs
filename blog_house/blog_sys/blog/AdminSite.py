from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    # 自定义管理后台
    site_header = 'Blog'
    site_title = 'Blog 管理后台'
    index_title = '作者后台'


custom_site = CustomSite(name='cus_admin')
