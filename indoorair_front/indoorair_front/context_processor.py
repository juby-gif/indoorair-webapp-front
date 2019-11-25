def extra_address_context_processor(request):
    return {
        'BACKEND_SERVER_ADDRESS' : 'http://127.0.0.1:8000'
    }
