APP_INF = {
    'title': 'Bootstrap学习笔记',
}

APP_INF.update({
    'META': {
        'DESCRIPTION': "基于Bootstrap样式的学习笔记",
        'AUTHOR': "Bootstrap学习笔记",
        'KEYWORDS': "Bootstrap,jQuery,jQuery UI,CSS,CSS框架,CSS framework,javascript,bootcss,bootstrap开发,bootstrap代码,"
                    "bootstrap入门",
        'ROBOTS': "index,follow",
        "APPLICATION-NAME": "bootstrap_learn.com",
    },
})

APP_INF.update({
    'NAV': {
        'brand': {
            'content': 'Bootstrap学习笔记',
            'url': '#',
        },
        'menu': {
            '首页': {
                'url': '',
                'class': 'nav-link',
                'current': True,
            },
            '笔记': {
                'url': 'note',
                'class': 'nav-link',
                'current': False,
            },
            '案例': {
                'url': 'example',
                'current': False,
                'class': 'nav-link dropdown-toggle',
                'dropdown-menu': {
                    'Action1': {'url': '#', 'class': "dropdown-item"},
                    'Action2': {'url': '#', 'class': "dropdown-item"},
                    'Action3': {'url': '#', 'class': "dropdown-item"},
                },
            },
        },
    },
})
