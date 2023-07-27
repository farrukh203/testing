# testing
This directory show three different project
1. gs1
2. custom_middleware
3. custom_admin

project gs1 (app_name api):
    In this project we made a serializer and also  used authentication and 
    permissions classes. In which we serialize our model and apply 
    BasicAuthentication on user login with assign some permission to
    apply CRUD operations.

project custom_middleware (app_name my_app):
    Create a file middleware_test in my_app in which we create custom
    middleware classes with the name MYProcessMiddleware, MyExceptionMiddleware
    and MyTemplateResponseMiddleware to handle HttpRequest by these
    middleware classes.
    
    **__init__(self, get_response)**
    django initialize middleware get_response callable and returns a
    middleware or actual view it is call one time as server run.
    
    **__call__**
    it is call once per request and return response
    
    **process_view(self, request, *args, **kwargs)**
    it is call before django call to appropriate view. return HttpResponse object or None.
    If None django execute next process_view of middleware or view if it is last
    middleware. Otherwise return HttpResponse
    
    process_exception(self, request, exception):
    it is call after django call to appropriate view and view raise an exception.
    return HttpResponse object or None. If None django execute middleware in reverse
    response order Handle view exception using this method.

    **process_template_response(self, request, response)**
    In this method we can change template_response data using 'context_data' and send
    response to client.

project custom_admin (app_name my_app):
    create a Students, Course and Grade model to save student information, Course detail
    and student Grade.
    register all above models in admin module using @admin.register(model_name) decorator. 
    change admin header using admin.site.site_header in admin.py file.
    change admin site title using admin.site.index_title in admin.py file.
    Create classes StudentAdmin, CourseAdmin and GradeAdmin subclass of admin.ModelAdmin
    in admin.py file
    