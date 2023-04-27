'''
def middlewarename(get_response):
    code to be written that need to 
    be executed only once i.e
    for initialization or for 
    configuration.

    def your_functionname(request):
        code need to be executed before views function 
        is called.
        variable=get_response(request)
        code need to be executed after views function is called

        return variable

return your_functionname
    

'''

def blog_middleware(get_response):
    print("blog_middleware function is inoked when server runs")
    print("Code need to be executed only once for initialization or configuration")

    def my_middleware(request):
        print("hello before view function is called...")
        res=get_response(request)
        print(res)

        print("hello from middleware after view funtion is")
        return res
    return my_middleware