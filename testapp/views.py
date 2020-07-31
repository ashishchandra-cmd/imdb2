from django.shortcuts import render
from testapp.models import Movies
from  django.views.generic import ListView , DetailView ,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#for customer
class MoviesListView(ListView):
    model = Movies
    paginate_by = 2
    #template_name=movies_list.html
    #context_object=movies_list
class MoviesDetailView(DetailView):
    model = Movies
    # template_name=movies_detail.html
    # context_object=movies or object

#for admin
def movieslist(request):
    movie=Movies.objects.all()
    return render(request,'testapp/movieslist.html' ,{'movie':movie})
class MoviesCreateView(CreateView):
    model = Movies
    fields = '__all__'
class MoviesUpdateView(UpdateView):
    model = Movies
    fields = '__all__'

class  MoviesDeleteView(DeleteView):
    model = Movies
    success_url = reverse_lazy('list_page_show')


from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
def search_title_view(request):
    if request.method=='POST':
        til=request.POST['search_title']
    else:
        til=''
    articles=Movies.objects.filter(Title__icontains=til)
    print(articles)
    return render(request,'testapp/ajax_search.html',{'articles':articles})
