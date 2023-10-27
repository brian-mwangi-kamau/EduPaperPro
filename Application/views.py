from django.shortcuts import render, redirect
from django.http import HttpResponse
from Application.forms import ResourceForm
from django.shortcuts import get_object_or_404
from .models import Resource
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Users.models import CustomUser
from django.db.models import Count
from django.db.models import Count
from django.urls import reverse_lazy
from django.db.models import Q
from Users.models import CustomUser
from .forms import UpdateForm


def landing_page(request):
    resources = Resource.objects.filter(is_free=True)

    context = {
        'resources': resources,
    }

    return render(request, 'landing_page.html', context)


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('profile')
    else:
        form = UpdateForm(initial={'first_name': user.first_name, 'last_name': user.last_name})

    return render(request, 'profile.html', {
        'user': user,
        'form': form,
    })




@login_required
def dashboard(request):
    user = request.user
    if user.is_staff:
        users = CustomUser.objects.count()
        active_users = CustomUser.objects.filter(is_active=True).count()
        subscribed_users = CustomUser.objects.filter(is_subscribed=True).count()
        education_counts = CustomUser.objects.values('level_of_education').annotate(count=Count('level_of_education'))
        education_data = list(education_counts)

        context = {
            'users': users,
            'active_users': active_users,
            'subscribed_users': subscribed_users,
            'education_data': education_data,
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


def filter_items(request):
    category = request.GET.get('level_of_education', 'All')

    if category == 'All':
        resources = Resource.objects.all()
    else:
        resources = Resource.objects.filter(category=category)

    resource_list = [resource.title for resource in resources]
    return JsonResponse({'resources': resource_list})




@login_required
def admin_resources(request):
    user = request.user
    if user.is_staff:
        resources = Resource.objects.all()

        context = {
            'resources': resources,
        }
        return render(request, 'admin_resources.html', context)
    else:
        return HttpResponse("You cannot perform this action!")
    



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
    file_path = form_file.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{form_file.file.name}"'
        return response
    

def preview_description(request, form_id):
    form_file = get_object_or_404(Resource, id=form_id)
    return render(request, 'preview_description.html', {'form_file': form_file})



@login_required
def delete_resource(request, form_id):
    user = request.user
    if user.is_staff:
        resource = Resource.objects.get(pk=form_id)
        resource.delete()
        return redirect('admin_resources')
    else:
        return HttpResponse("You cannot perform this action!")



@login_required
def update_resource(request, form_id):
    resource = Resource.objects.get(pk=form_id)
    form = ResourceForm(request.POST or request.FILES or None, instance=resource)
    user = request.user
    if user.is_staff:
        if form.is_valid():
            form.save()
            return redirect('admin_resources')
        
        return render(request, 'update_resource.html', {
            'resource': resource,
            'form': form,
        })
    else:
        return HttpResponse("You cannot perform this action!")


