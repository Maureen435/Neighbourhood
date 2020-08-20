from django.shortcuts import render
from django.template import RequestContext

@csrf_protect
def register(request):
    # ...

    return render_to_response(
        'register.html',
        {'form': form}, 
        RequestContext(request)
    )