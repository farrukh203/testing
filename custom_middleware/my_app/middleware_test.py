from django.shortcuts import HttpResponse

class MyProcessMiddleware(object):
    def __init__(self, get_response):
        """
        django initialize middleware
        get_response callable and returns a middleware or actual view
        it is call one time as server run
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        it is call once per request and return response
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        """
        it is call before django call to appropriate view.
        return HttpResponse object or None. If None django execute next process_view of middleware
        or view if it is last middleware. Otherwise return HttpResponse
        """
        print("This is process view call before view")
        #return HttpResponse("This is process_view response")
        return None

class MyExceptionMiddleware(object):
    def __init__(self, get_response):
        """
        django initialize middleware
        get_response callable and returns a middleware or actual view
        it is call one time as server run
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        it is call once per request and return response
        """
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """
        it is call after django call to appropriate view and view raise an exception.
        return HttpResponse object or None. If None django execute middleware in reverse response order
        Handle view exception using this method.
        """
        print("Exception occur")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)


class MyTemplateResponseMiddleware(object):
    def __init__(self, get_response):
        """
        django initialize middleware
        get_response callable and returns a middleware or actual view
        it is call one time as server run
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        it is call once per request and return response
        """
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data['name'] = 'rizwan'
        return response


# function based middleware

#def my_middleware(get_response):
#    print("One time configuration and initalization")

#    def my_middleware_function(request):
#        print("This is before view")
#        response = get_response(request)
#        print(("This is after view"))

#        return response
#    return my_middleware_function