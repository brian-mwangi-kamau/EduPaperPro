from django.shortcuts import render, redirect
from django.http import HttpResponse
from Application.forms import ResourceForm
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import DownloadRecord, Resource
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Users.models import CustomUser
from django.db.models import Count
from django.db.models.functions import TruncDate, TruncMonth
from django.utils import timezone
from datetime import timedelta



def landing_page(request):
    return render(request, 'landing_page.html')



@login_required
def dashboard(request):
    user = request.user
    if user.is_staff:
        users = CustomUser.objects.count()
        user_downloads = DownloadRecord.objects.count()

        context = {
            'users': users,
            'downloads': user_downloads,
        }
        return render(request, 'admin_dashboard.html', context)
    else:
        name = request.user.first_name
        if user.is_subscribed:
            resources = Resource.objects.all()
        else:
            resources = Resource.objects.filter(is_free=True)

        context = {
            'name': name,
            'resources': resources,
        }

        return render(request, 'dashboard.html', context)



def upload_form(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = ResourceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('form_upload')
        else:
            form = ResourceForm()
        return render(request, 'forms/forms_upload.html', {'form': form})
    else:
        return HttpResponse("You cannot perform this action!")



def record_download(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        form_file = get_object_or_404(Resource, id=form_id)
        DownloadRecord.objects.create(resource=form_file)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def download_forms(request, form_id):
    form_file = get_object_or_404(Resource, id=form_id)
    file_path = form_file.file.path
    DownloadRecord.objects.create(resource=form_file)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{form_file.file.name}"'
        return response
    


def platform_metrics(request):
    total_users = CustomUser.objects.count()

    return JsonResponse({'total_users': total_users},)


def download_data(request):
    download_data = DownloadRecord.objects.annotate(
        download_day=TruncDate('timestamp')
    ).values('download_day').annotate(
        download_count=Count('id')
    )

    data = {
        'downloads': [
            {
                'date': record['download_day'].strftime('%Y-%m-%d'),
                'count': record['download_count']
            }
            for record in download_data
        ]
    }

    return JsonResponse(data)
   