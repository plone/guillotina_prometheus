from prometheus_client import Counter
from prometheus_client import Summary


request_summary = Summary('guillotina_request_processing', 'Time spent processing request')
request_counts = Counter('guillotina_request_counts', 'Number and type of requests',
                         ['method', 'view', 'response_code'])
