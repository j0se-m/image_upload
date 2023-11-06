from django.shortcuts import render, redirect,get_object_or_404
from .models import Image
from .forms import ImageForm


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('image_list')
    else:
        form = ImageForm()
        return render(request, 'upload_image.html', {'form': form})


def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

# def update_image(request, id):
#     image = get_object_or_404(Image, id=id)
#     if request.method == 'POST':
#         form =  ImageForm(request.POST, instance=image)
#         if form.is_valid():
#             form.save()
#             return redirect('image_list')
#
#     else:
#         form = ImageForm(instance=image)
#         return render(request, 'image_list.html', {'form': form})
#
#
# def delete_image(request, id):
#     image= get_object_or_404(Image, id=id)
#     image.delete()
#     return redirect('image_list')
