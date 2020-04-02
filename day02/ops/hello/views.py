from django.shortcuts import render
from hello.models import Asset
# Create your views here.
from django.http import HttpResponse,QueryDict,HttpResponseRedirect


def asset_add(request):
    if request.method == 'POST':
        data = request.POST
        ip = data.get('ip')
        hostname = data.get('hostname')
        data1 = {'ip': ip, 'hostname': hostname }
        # print(data1)
        try:
            Asset.objects.create(**data1)
        except Exception as e:
            return  HttpResponse(e)
        return HttpResponseRedirect('/hello/')
    else:
        return render(request, 'hello/add.html')


def asset_update(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    if request.method == 'POST':
        data = request.POST
        # print(type(data))
        ip = data.get('ip')
        hostname = data.get('hostname')
        data1 = {'ip': ip, 'hostname': hostname}
        try:
            Asset.objects.filter(id=asset_id).update(**data1)
        except Exception as e:
            return  HttpResponse(e)
        return HttpResponseRedirect('/hello/')
    else:
        return render(request, 'hello/update.html', {'Asset': asset})



def asset_delete(request, asset_id):
    # asset = Asset.objects.get(id=asset_id)
    if request.method == 'POST':
        try:
            Asset.objects.filter(id=int(asset_id)).delete()
        except Exception as e:
            return  HttpResponse(e)
        return HttpResponseRedirect('/hello/')
    else:
        return HttpResponse('404')



def asset_list(request):
    asset = Asset.objects.all()
    return render(request, 'hello/list.html', {'Asset': asset})



