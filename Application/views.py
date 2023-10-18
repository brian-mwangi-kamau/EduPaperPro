from django.shortcuts import render, redirect
from django.http import HttpResponse
from Application.forms import ResourceForm
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Resource
from django.contrib.auth.decorators import login_required



def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def dashboard(request):
    user = request.user
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




def download_forms(request, form_id):
        form_file = get_object_or_404(Resource, id=form_id)
        file_path = form_file.form.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True)