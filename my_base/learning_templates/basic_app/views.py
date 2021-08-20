from django.shortcuts import render

# Create your views here.

# For index
def index(request):
    context_dict = {'text': 'hello world','number': 100}
    return render(request,'basic_app/index.html', context_dict)
# For Other
def other(request):
    return render(request,'basic_app/other.html')
# For relative_url_templates
def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
