""" views.py """

from django.views import generic


class IndexView(generic.RedirectView):
    """ IndexView """
    permanent = True
    url = "/polls/"
