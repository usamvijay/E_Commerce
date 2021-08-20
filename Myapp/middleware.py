def auth_middleware(get_response):

    def middleware(request):
        print('vijay')
      

        response = get_response(request)



        return response

    return middleware
