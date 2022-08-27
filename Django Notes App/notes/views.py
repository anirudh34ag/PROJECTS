from django.shortcuts import render
from .models import Notes 
from django.http import Http404
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .forms import NotesForm 
from django.views.generic.edit import DeleteView 
from .models import Notes
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http.response import HttpResponseRedirect 


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes 
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesListView(LoginRequiredMixin, ListView):
    model = Notes 
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# -------before using classes ------
#def list(request):
#    all_notes = Notes.objects.all()
#    return render(request, 'notes/notes_list.html',{'notes':all_notes})
 
def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist!")
    return render(request, 'notes/notes_detail.html',{'note': note})
# Create your views here.
