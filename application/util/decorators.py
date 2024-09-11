def handle_exception(func):

    def wrapper_function(self, *args, **kwargs):
        func_result = func(self, *args, **kwargs)
        print(type(func_result))
        if type(func_result) == dict:
            if func_result.get("status") == 400:
                print("invalid url link")

        print("handle exception called ")
        return func_result

    return wrapper_function
