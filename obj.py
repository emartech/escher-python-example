import datetime
from escherauth import Escher

request = {
    'method': 'GET',
    'host': 'host.foo.com',
    'uri': '/?foo=bar',
    'headers': [
        ('Date', 'Mon, 09 Sep 2011 23:36:00 GMT'),
        ('Host', 'host.foo.com'),
    ],
}
escher = Escher('us-east-1/host/aws4_request', {
    'algo_prefix': 'AWS4',
    'vendor_key': 'AWS4',
    'hash_algo': 'SHA256',
    'auth_header_name': 'Authorization',
    'date_header_name': 'Date',
    'current_time': datetime.datetime(2011, 9, 9, 23, 36)
})

request = escher.sign(request, {'api_key': 'AKIDEXAMPLE', 'api_secret': 'wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY'})

print request