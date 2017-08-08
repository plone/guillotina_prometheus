from guillotina_prometheus import metrics
from prometheus_async.aio import time
from guillotina.utils import get_dotted_name


async def middleware_factory(app, handler):
    @time(metrics.request_summary)
    async def middleware_handler(request):
        resp = await handler(request)
        try:
            user_id = request.security.principal.id
        except AttributeError:
            user_id = 'unknown'

        try:
            try:
                view_name = get_dotted_name(request.found_view.view_func)
            except AttributeError:
                view_name = get_dotted_name(request.found_view)
        except AttributeError:
            view_name = 'unknown'
        metrics.request_counts.labels(
            method=request.method,
            view=view_name,
            response_code=resp.status,
            user_id=user_id).inc()
        return resp
    return middleware_handler
