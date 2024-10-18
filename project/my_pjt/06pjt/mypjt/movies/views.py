from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    movies = Movie.objects.all().order_by('-created_at')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_http_methods(["GET"])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'form': form,
            'movie': movie,
        }
        return render(request, 'movies/update.html', context)
    else:
        return redirect('movies:index')

@login_required
@require_http_methods(["POST"])
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')

@login_required
@require_http_methods(["POST"])
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movies:detail', movie.pk)

@login_required
@require_http_methods(["POST"])
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('movies:detail', movie_pk)

@require_http_methods(["POST"])    
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.like_user.all():
        # 이미 좋아요를 누른 상태이므로 좋아요 취소
        movie.like_user.remove(request.user)
    else:
        # 아직 좋아요 누르지 않은 상태
        movie.like_user.add(request.user)
    return redirect('movies:index')