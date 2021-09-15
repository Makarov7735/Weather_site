
def check_cookies_count(request, response):
    if len(request.COOKIES) > 5:
        all_cookies = list(request.COOKIES.keys())
        print(all_cookies)
        response.delete_cookie(all_cookies[0]) 
    

def set_cookies(request, response, context):
    for i in request.COOKIES:
        if not 'city' in i:
            response.delete_cookie(i) 

    if len(request.COOKIES) < 1:
        response.set_cookie('city1', context['city'])
    else:
        if len(request.COOKIES) == 1 and not '1' in list(request.COOKIES.keys())[0]:
            last_cookie = list(request.COOKIES.values())[0]
            response.delete_cookie(list(request.COOKIES.keys())[0])
            response.set_cookie('city1', last_cookie)

        if context['city'] not in request.COOKIES.values():
            response.set_cookie(f'city{len(request.COOKIES)+1}', context['city'])
