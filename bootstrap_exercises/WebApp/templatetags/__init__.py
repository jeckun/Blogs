from django.forms import Media


vendors = {
    "bootstrap": {
        'js': {
            'dev': 'xadmin/vendor/bootstrap/js/bootstrap.js',
            'production': 'xadmin/vendor/bootstrap/js/bootstrap.min.js',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js'
        },
        'scss': {
            'dev': 'xadmin/vendor/bootstrap/scss/bootstrap.scss',
            'production': 'xadmin/vendor/bootstrap/scss/bootstrap.scss',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css'
        },
        'responsive': {'scss':{
                'dev': 'xadmin/vendor/bootstrap/bootstrap-responsive.scss',
                'production': 'xadmin/vendor/bootstrap/bootstrap-responsive.scss'
            }}
    },
    'jquery': {
        "js": {
            'dev': 'xadmin/vendor/jquery/jquery.js',
            'production': 'xadmin/vendor/jquery/jquery.min.js',
        }
    },
    'jquery-ui-effect': {
        "js": {
            'dev': 'xadmin/vendor/jquery-ui/jquery.ui.effect.js',
            'production': 'xadmin/vendor/jquery-ui/jquery.ui.effect.min.js'
        }
    },
    'jquery-ui-sortable': {
        "js": {
            'dev': ['xadmin/vendor/jquery-ui/jquery.ui.core.js', 'xadmin/vendor/jquery-ui/jquery.ui.widget.js',
                    'xadmin/vendor/jquery-ui/jquery.ui.mouse.js', 'xadmin/vendor/jquery-ui/jquery.ui.sortable.js'],
            'production': ['xadmin/vendor/jquery-ui/jquery.ui.core.min.js', 'xadmin/vendor/jquery-ui/jquery.ui.widget.min.js',
                           'xadmin/vendor/jquery-ui/jquery.ui.mouse.min.js', 'xadmin/vendor/jquery-ui/jquery.ui.sortable.min.js']
        }
    },
    "font-awesome": {
        "scss": {
            'dev': 'xadmin/vendor/font-awesome/scss/font-awesome.scss',
            'production': 'xadmin/vendor/font-awesome/scss/font-awesome.min.scss',
        }
    },
    "timepicker": {
        "scss": {
            'dev': 'xadmin/vendor/bootstrap-timepicker/scss/bootstrap-timepicker.scss',
            'production': 'xadmin/vendor/bootstrap-timepicker/scss/bootstrap-timepicker.min.scss',
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.js',
            'production': 'xadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.min.js',
        }
    },
    "clockpicker": {
        "scss": {
            'dev': 'xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.scss',
            'production': 'xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.min.scss',
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.js',
            'production': 'xadmin/vendor/bootstrap-clockpicker/bootstrap-clockpicker.min.js',
        }
    },
    "datepicker": {
        "scss": {
            'dev': 'xadmin/vendor/bootstrap-datepicker/scss/datepicker.scss'
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-datepicker/js/bootstrap-datepicker.js',
        }
    },
    "flot": {
        "js": {
            'dev': ['xadmin/vendor/flot/jquery.flot.js', 'xadmin/vendor/flot/jquery.flot.pie.js', 'xadmin/vendor/flot/jquery.flot.time.js',
                    'xadmin/vendor/flot/jquery.flot.resize.js','xadmin/vendor/flot/jquery.flot.aggregate.js','xadmin/vendor/flot/jquery.flot.categories.js']
        }
    },
    "image-gallery": {
        "scss": {
            'dev': 'xadmin/vendor/bootstrap-image-gallery/scss/bootstrap-image-gallery.scss',
            'production': 'xadmin/vendor/bootstrap-image-gallery/scss/bootstrap-image-gallery.scss',
        },
        "js": {
            'dev': ['xadmin/vendor/load-image/load-image.js', 'xadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js'],
            'production': ['xadmin/vendor/load-image/load-image.min.js', 'xadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js']
        }
    },
    "select": {
        "scss": {
            'dev': ['xadmin/vendor/select2/select2.scss', 'xadmin/vendor/selectize/selectize.scss', 'xadmin/vendor/selectize/selectize.bootstrap3.scss'],
        },
        "js": {
            'dev': ['xadmin/vendor/selectize/selectize.js', 'xadmin/vendor/select2/select2.js', 'xadmin/vendor/select2/select2_locale_%(lang)s.js'],
            'production': ['xadmin/vendor/selectize/selectize.min.js', 'xadmin/vendor/select2/select2.min.js', 'xadmin/vendor/select2/select2_locale_%(lang)s.js']
        }
    },
    "multiselect": {
        "scss": {
            'dev': 'xadmin/vendor/bootstrap-multiselect/scss/bootstrap-multiselect.scss',
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-multiselect/js/bootstrap-multiselect.js',
        }
    },
    "snapjs": {
        "scss": {
            'dev': 'xadmin/vendor/snapjs/snap.scss',
        },
        "js": {
            'dev': 'xadmin/vendor/snapjs/snap.js',
        }
    },
}


def xstatic(*tags):
    # from .vendors import vendors
    node = vendors

    fs = []
    lang = get_language()

    cls_str = str if six.PY3 else basestring
    for tag in tags:
        try:
            for p in tag.split('.'):
                node = node[p]
        except Exception as e:
            if tag.startswith('xadmin'):
                file_type = tag.split('.')[-1]
                if file_type in ('scss', 'js'):
                    node = "xadmin/%s/%s" % (file_type, tag)
                else:
                    raise e
            else:
                raise e

        if isinstance(node, cls_str):
            files = node
        else:
            mode = 'dev'
            if not settings.DEBUG:
                mode = getattr(settings, 'STATIC_USE_CDN',
                               False) and 'cdn' or 'production'

            if mode == 'cdn' and mode not in node:
                mode = 'production'
            if mode == 'production' and mode not in node:
                mode = 'dev'
            files = node[mode]

        files = type(files) in (list, tuple) and files or [files, ]
        fs.extend([f % {'lang': lang.replace('_', '-')} for f in files])

    return [f.startswith('http://') and f or static(f) for f in fs]


def vendor(*tags):
    css = {'screen': []}
    js = []
    for tag in tags:
        file_type = tag.split('.')[-1]
        files = xstatic(tag)
        if file_type == 'js':
            js.extend(files)
        elif file_type == 'scss':
            css['screen'] += files
    return Media(css=css, js=js)
