from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import newForm
from .models import bitlyURL


# Create your views here.
def redirect_view(request, shortcode=None, *args, **kwargs):
    obj = bitlyURL.objects.filter(shortcode__iexact=shortcode)
    if obj.exists():
        obj = get_object_or_404(bitlyURL, shortcode__iexact=shortcode)
        obj.count += 1
        obj.save()
        return HttpResponseRedirect(obj.url)
    else:
        return render(request, "404.html", {})


def home_view(request):
    form = newForm(request.POST or None)

    if form.is_valid():
        new_url = form.cleaned_data['url']
        obj, created = bitlyURL.objects.get_or_create(url=new_url)
        context = {
            "created": created,
            "object": obj,
        }
        if created:
            return render(request, "success.html", context)
        else:
            return render(request, "already_exists.html", context)

    context = {
        "form": form,
        "title": "Welcome",
    }
    return render(request, "home.html", context)