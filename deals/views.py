from django.shortcuts import render
from collections import OrderedDict
import requests
from .forms import SubmitDeal

def find_deal(request):
    if request.method == "POST":
        form = SubmitDeal(request.POST)

        if form.is_valid():
            params = OrderedDict([('scenario', 'deal-finder'), ('page', 'foo'), ('uid', 'foo'), ('productType', 'Hotel')])
            params.update(form.cleaned_data)

            r = requests.get('https://offersvc.expedia.com/offers/v2/getOffers', params=params)
            deal= r.json()
            return render(request, 'deals.html', {'deal': deal})

    else:
        form = SubmitDeal()
    return render(request, 'index.html', {'form': form})

