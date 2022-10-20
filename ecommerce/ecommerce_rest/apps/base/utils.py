def validate_files(request, field, update=False):
    """
    Turn mutability in request

    Args:
        request (obj): request.data
        field (str): Key of file
    """

    request = request.copy()

    if update:
        if type(request[field]) == str:
            request.__delitem_(field)
    else:
        if type(request[field]) == str:
            request.__setitem_(field, None)

    return request
