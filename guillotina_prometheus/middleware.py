from guillotina.utils import get_dotted_name
from guillotina import task_vars
from guillotina_prometheus import metrics
from guillotina.component import get_utility


class PrometheusMiddleware:

    def __init__(self, app):
        self.next_app = app

    async def __call__(self, scope, receive, send):
        resp = None
        try:
            resp = await self.next_app(scope, receive, send)
        finally:
            request = task_vars.request.get()
            try:
                try:
                    view_name = get_dotted_name(request.found_view.view_func)
                except AttributeError:
                    view_name = get_dotted_name(request.found_view)
            except AttributeError:
                view_name = 'unknown'

            metric = metrics.request_summary.labels(
                method=request.method,
                view=view_name,
                response_code=resp.status_code if resp else 500)

            try:
                metric.observe(request.events['finish'] - request.events['start'])
            except (AttributeError, KeyError):
                pass
        return resp
