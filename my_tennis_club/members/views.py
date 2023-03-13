from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

#def members(request):
#  template = loader.get_template('hi.html')
#  return HttpResponse(template.render())




#from django.http import HttpResponse

#def members(request):
#    return HttpResponse("Hello There !")
