from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Hello, Django!")

def taskstring(request):
    result = 'Rest API stinrg!'
    return HttpResponse(result)

def taskxml(request):
    result = '<employees>   \
                <employee>  \
                    <firstName>John</firstName> <lastName>Doe</lastName>    \
                </employee> \
                <employee>  \
                <firstName>Anna</firstName> <lastName>Smith</lastName>    \
                </employee> \
            </employees>'
    return HttpResponse(result, content_type='text/xml')

def taskjson(request):
    result = {"employees":[    
                { "firstName":"John", "lastName":"Doe" },   
                { "firstName":"Anna", "lastName":"Smith" }, 
                { "firstName":"Peter", "lastName":"Jones" } 
            ]}
    return JsonResponse(result)
