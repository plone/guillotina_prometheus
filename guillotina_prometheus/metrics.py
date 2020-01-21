from prometheus_client import Histogram

request_summary = Histogram(
    'http_request',
    'Time spent processing request',
    ['method', 'view', 'response_code'],
    buckets=[0.0005, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.4, 0.6, 0.8, 1, 2, float("inf")],
)
