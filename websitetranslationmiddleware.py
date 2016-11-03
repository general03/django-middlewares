from django.utils import translation
from django.shortcuts import HttpResponsePermanentRedirect

"""
Middleware for user language preference.
Sets the user's language preference on the session, if it is not already set.
"""
class WebsiteTranslationMiddleware(object):

    """ Set the language preference, if any, on the session. """
    def process_request(self, request):

    # Check if request to change lang
		languagePost = request.POST.get("language")
    	
		cur_language = translation.get_language()

		url = request.META['HTTP_HOST']
		domain = url.split('.')[0]
		extension = url.split('.')[1]

		if '127.0.0.1' in url:
			extension = cur_language
		elif extension not in ('fr', 'com'):
			raise ImproperlyConfigured

		if languagePost is None:
			translation.activate(extension)
		else:
			translation.activate(languagePost)

		if '127.0.0.1' not in url:
			if extension not in cur_language:
				return HttpResponsePermanentRedirect('http://'+domain+'.'+extension)

			if extension not in languagePost:
				return HttpResponsePermanentRedirect('http://'+domain+'.'+extension)
