from django.shortcuts import render
from django.urls import path
from django.template import loader
from django.db.models import Max
from . import views
from .models import claim, user_validation
import random
from validation_app.forms import validate

def index(request):
    template = loader.get_template('validation_app/index.html')
    max_claim = claim.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_claim)
    claim_to_validate = claim.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = validate(request.POST)
        if form.is_valid():
            related = form.cleaned_data['related']
            claims = form.cleaned_data['claim']
            claim_text = claim_to_validate
            u = user_validation(claim_text=claim_text, related=related, claim=claims)
            u.save()
            form = validate()
            context = {'claim_to_validate' : claim_to_validate,
                        'form' : form}
            return render(request, "validation_app/index.html", context)
    else:
        form = validate()
        context = {'claim_to_validate' : claim_to_validate,
                    'form' : form}
        return render(request, "validation_app/index.html", context)

