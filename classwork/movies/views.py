from django.shortcuts import render
from .forms import MovieForm

def movie_view(request):
    message = None
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            message = f"Movie saved: {movie.name} ({movie.year})"
            form = MovieForm()  # clear the form after saving
    else:
        form = MovieForm()

    return render(request, "movies/movie.html", {"form": form, "message": message})
