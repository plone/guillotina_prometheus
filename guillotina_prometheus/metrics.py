from prometheus_client import Counter
from prometheus_client import Summary


request_summary = Summary('request_processing', 'Time spent processing request')
request_counts = Counter('request_counts', 'Number and type of requests',
                         ['method', 'view', 'response_code'])
