APP_INF = {
    'title': "Jeckun's Tech Tree",
}

APP_INF.update({
    'META': {
        'DESCRIPTION': "Python+Django+Bootstrap",
        'AUTHOR': "Eric",
        'KEYWORDS': "Bootstrap,jQuery,jQuery UI,CSS,CSS框架,CSS framework,javascript,bootcss,bootstrap开发,bootstrap代码,"
                    "bootstrap入门",
        'ROBOTS': "index,follow",
        "APPLICATION-NAME": "bootstrap_learn.com",
    },
})

APP_INF.update({
    'NAV': {
        'brand': {
            'content': "Tech Tree",
            'url': '#',
        },
        'menu': {
            '首页': {
                'url': 'index',
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
                'class': 'nav-link',
            },
        },
    },
})

APP_INF.update({
    'CHANNEL': {
        'index': {
            'title': 'Tech Tree',
            'content': "这是一个关于科技树的网址，每个人可以整理、建立、分享自己的科技树，可以补充完善别人的科技树，最终汇集"
                       "大家的智慧形成某一类人的科技树。以此帮助哪些需要这些知识的人们，快速找到、学习和构建自己的科技树。我"
                       "们的初衷是燃烧自己，照亮别人，在点滴的累计中，丰富巩固人类的科技成果，并且进行传承。",
        },
        'note': {
            'title': 'Python+Django+Bootstrap',
            'content': '这里是学习BootStrap过程中累计的经验和技巧，欢迎各位同学交流。',
        },
        'example': {
            'title': '实例精选',
            'content': '以下实例全部基于前面所讲的基本模板并配合 Bootstrap 的众多组件开发而成。我们鼓励你根据自身项目的需要对 Bootstrap 进行定制和修改。',
        },
    }
})

APP_INF.update({
    'About': "关于我为什么要学习Bootstrap，我仔细想了好久，发现我缺少一种可以快速变现的工具，而Bootstrap这个前端工具"
             "可以很好的帮我实现我想要做的一些好点子。",
})