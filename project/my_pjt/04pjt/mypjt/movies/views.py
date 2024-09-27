from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['Movie_image']  # Movie_image 사용
            
            # Pillow를 사용하여 이미지 리사이즈
            img = PilImage.open(image_file)
            img = img.resize((300, 400), PilImage.LANCZOS)  # 원하는 크기로 변경
            
            # BytesIO를 사용하여 이미지를 메모리에 저장
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG')  # 원하는 포맷으로 저장
            img_file = ContentFile(img_io.getvalue(), name=image_file.name)

            # Movie 인스턴스 생성
            movie = form.save(commit=False)
            movie.Movie_image = img_file  # 리사이즈된 이미지 할당
            movie.save()  # 저장
            
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            if 'Movie_image' in request.FILES:  # Movie_image 필드 체크
                image_file = form.cleaned_data['Movie_image']
                
                # Pillow를 사용하여 이미지 리사이즈
                img = PilImage.open(image_file)
                img = img.resize((300, 400), PilImage.LANCZOS)  # 원하는 크기로 변경
                
                # BytesIO를 사용하여 이미지를 메모리에 저장
                img_io = io.BytesIO()
                img.save(img_io, format='JPEG')
                img_file = ContentFile(img_io.getvalue(), name=image_file.name)

                movie.Movie_image = img_file  # 리사이즈된 이미지 할당
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)