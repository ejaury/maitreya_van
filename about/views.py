from django.shortcuts import render_to_response

def contact_us(request):
  return render_to_response('about/contact_us.html')

