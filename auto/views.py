from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .autoEv import PJ
from .getScore import score
from django.views.decorators.csrf import csrf_exempt
import logging
import sys

logger= logging.getLogger("Chenshufu")
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stderr)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

@csrf_exempt
def input(request):
    if request.method == 'POST':
        print(request.POST['id'],request.POST['passwd'])
        if request.POST['t'] == 'pj':
            #res = PJ(request.POST['id'],request.POST['passwd']).run()#debug
            logger.warning("username" + request.POST['id'])
        else:
            res = score(request.POST['id'],request.POST['passwd']).run()
            logger.warning("score_username" + request.POST['id'])
        return render_to_response('res.html',{'res':res }, context_instance=RequestContext(request))
    else:
        test = ""
        return render_to_response('input.html',{'test': test}, context_instance=RequestContext(request))
