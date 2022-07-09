from django.urls import path
from . import views
from .views import SearchResultsView

app_name = "home"
urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('snippets/', SearchResultsView.as_view(), name="snippets_view"),
    path('snippet_code/<str:snip>', views.snippet_view, name="snippet_view"),
    path('snippet_code/edit/<str:snipedit>', views.edit_snippet, name="edit_snippet")
]
