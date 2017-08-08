from guillotina import configure
from guillotina_prometheus import middleware


app_settings = {
}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('guillotina_prometheus.api')
