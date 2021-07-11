from django.shortcuts import render
from django.http import JsonResponse
from json import load

def checker(request):
    context = {}
    if request.method == 'POST':
        code = request.POST.get('c', None)
        print(code)
        fl = False
        res = "код не существует"
        if code and len(code) <= 8:
            with open('checker/data_promo.json', 'r') as f:
                data = load(f)
                
            for item in data:
                item = dict(item)
                fl = code in item['promo'] 
                print(f'''
                    {fl} {code} {item['promo']}
                ''')
                if fl:
                    group = item['name'] 
                    res = f"код существует группа = {group}"
        context['res'] = res
    return render(request, 'checker/index.html', context)

# def check(request):
#     code = request.POST.get('c', None)
#     print(code)
#     fl = False
#     res = "код не существует"
#     if code and len(code) <= 8:
#         with open('checker/data_promo.json', 'r') as f:
#             data = load(f)
            
#         for item in data:
#             item = dict(item)
#             fl = code in item['promo'] 
#             print(f'''
#                 {fl} {code} {item['promo']}
#             ''')
#             if fl:
#                 group = item['name'] 
#                 res = f"код существует группа = {group}"
#     return JsonResponse({'foo': res})