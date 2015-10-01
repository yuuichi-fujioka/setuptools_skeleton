from oslo_config import cfg

default_opts = [
    cfg.StrOpt('foo', default='', help='foo value'),
]


egg_opts = [
    cfg.IntOpt('spam', default=99, help='spam value'),
]


CONF = cfg.CONF
CONF.register_opts(default_opts)
CONF.register_opts(egg_opts, group='egg')


def list_opts():
    return [
        ('DEFAULT', default_opts),
        ('egg', egg_opts),
    ]
