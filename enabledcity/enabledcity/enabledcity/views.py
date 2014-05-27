from django.shortcuts import render_to_response, RequestContext

from locations.models import Location

from .functions import foursquare_search


def home(request):
    if request.method == 'POST':
        print request.POST
        query = request.POST['search']
        locations = locu_search(query)
        for loc in locations:
            name, locu_id = loc[0], loc[1]
            new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
            if created:
                print "Created new id for %s with id of %s" %(name, locu_id)
        #locations = foursquare_search(query)
    
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))