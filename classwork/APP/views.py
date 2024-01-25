from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def run(request):
    return render(request, 'firstsite.html')
def main1(request):
    return render(request, 'firstsite2.html')
def main(request):
    return HttpResponseRedirect('main/')