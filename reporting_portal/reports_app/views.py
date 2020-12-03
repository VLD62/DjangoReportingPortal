from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from reports_core.decorators import group_required
from .forms import ReportCreateForm, FilterForm
from .models import Report


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }

def index(request):
    params = extract_filter_values(request.GET)
    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
    reports = Report.objects.filter(name__icontains=params['text']).order_by(order_by)
    context = {
        'reports': reports,
        'current_page': 'home',
        'filter_form': FilterForm()
    }

    return render(request, 'index.html', context)


@login_required(login_url='login user')
#@group_required(groups=['Regular Users'])
def create(request):
    if request.method == 'GET':
        context = {
            'form': ReportCreateForm(),
            'current_page': 'create',
        }
        return render(request, 'create.html', context)
    else:
        form = ReportCreateForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'current_page': 'create',
        }
        return render(request, 'create.html', context)

def report_details(request, pk):
    report = Report.objects.get(pk=pk)
    context = {
        'report': report,
    }
    return render(request, 'details.html', context)