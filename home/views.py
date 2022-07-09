from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView
from .models import Snippet
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home_view(request):
    if request.method == "POST":
        # print(request.POST.get("data"))
        return redirect("home:snippets_view")
    return render(request, "index.html")


@csrf_exempt
def snippets_view(request):
    if request.method == "get":
        snippets = Snippet.objects.filter(title__icontains=request.GET.get("data"))
        context = {"snippets": snippets}
        print(context)
        return render(request, "snippets_list.html", context)
    else:
        return render(request, "index.html")


class SearchResultsView(ListView):
    model = Snippet
    template_name = "snippets_list.html"

    @csrf_exempt
    def get_queryset(self):
        query = self.request.GET.get("data")
        print(query)
        return Snippet.objects.filter(title__icontains=query)

@csrf_exempt
def snippet_view(request, snip):
    snippet = Snippet.objects.get(title=snip)
    context = {'snippet': snippet}

    return render(request, "snippet_code.html", context)


def edit_snippet(request, snipedit):
    print("Edit Snip")