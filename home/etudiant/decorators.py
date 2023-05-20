from django.shortcuts import redirect 


def notLoginUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowedusers(allowedGroups=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedGroups:
                    return view_func(request, *args, **kwargs)
            else:
                return redirect("home")
        return wrapper_func
    return decorators

def Notallowedusers(NotallowedGroups=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            try:
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name
                if group in NotallowedGroups:
                    return redirect("home")
                else:
                    return view_func(request, *args, **kwargs)
            except:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorators