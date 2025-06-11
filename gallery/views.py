from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GalleryItemForm
from .models import GalleryItem

@login_required
def upload_gallery(request):
    if request.method == 'POST':
        formset = [GalleryItemForm(request.POST, request.FILES, prefix=str(i)) for i in range(1, 13)]
        all_valid = all(form.is_valid() for form in formset)
        if all_valid:
            for form in formset:
                form.save()
            return redirect('view_gallery')
        else:
            for i, form in enumerate(formset):
                print(f"Form {i+1} errors:", form.errors)
    else:
        formset = [GalleryItemForm(prefix=str(i)) for i in range(1, 13)]
    return render(request, 'gallery/upload.html', {'formset': formset})

@login_required
def view_gallery(request):
    if request.method == 'POST' and 'delete_all' in request.POST:
        GalleryItem.objects.all().delete()
        return redirect('view_gallery')

    items = GalleryItem.objects.all()
    return render(request, 'gallery/gallery.html', {'items': items})
