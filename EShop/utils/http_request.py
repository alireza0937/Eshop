from django.http import HttpRequest


def get_client_ip(request: HttpRequest):
    HTTP_X_FORWARDED_FOR = request.META.get('HTTP_X_FORWARDED_FOR')
    if HTTP_X_FORWARDED_FOR is not None:
        ip = HTTP_X_FORWARDED_FOR.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


