from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from reports_core.decorators import group_required
from reports_core.view_mixins import GroupRequiredMixin
from .forms import ReportCreateForm, FilterForm #,ReportDeleteForm
from .models import Report


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }

# def index(request):
#     params = extract_filter_values(request.GET)
#     order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
#     reports = Report.objects.filter(name__icontains=params['text']).order_by(order_by)
#     context = {
#         'reports': reports,
#         'current_page': 'home',
#         'filter_form': FilterForm()
#     }
#
#     return render(request, 'index.html', context)

#@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'index.html'
    model = Report
    context_object_name = 'reports'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)

        return result


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })

        return context

# @login_required(login_url='login user')
# #@group_required(groups=['Regular Users'])
# def create(request):
#     if request.method == 'GET':
#         context = {
#             'form': ReportCreateForm(),
#             'current_page': 'create',
#         }
#         return render(request, 'create.html', context)
#     else:
#         form = ReportCreateForm(request.POST, request.FILES,)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         context = {
#             'form': form,
#             'current_page': 'create',
#         }
#         return render(request, 'create.html', context)
#

#@method_decorator(group_required(groups=['Regular User']), name='dispatch')
#@method_decorator(login_required, name='dispatch')
class ReportCreateView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    form_class = ReportCreateForm
    template_name = 'actions/create.html'
    success_url = reverse_lazy('index')
    #TODO: add different groups maybe?
    groups = ['Regular_Users']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ReportDetailsView(DetailView):
    model = Report
    template_name = 'details.html'
    context_object_name = 'report'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report = context['report']
        context['heading_text'] = f'{report.name}'
        return context

# def report_details(request, pk):
#     report = Report.objects.get(pk=pk)
#     context = {
#         'report': report,
#     }
#     return render(request, 'details.html', context)


#Add to be member of specific group
#@method_decorator(login_required, name='dispatch')
# def edit_report(request, pk):
#     report = Report.objects.get(pk=pk)
# #    groups = ['Regular_Users']
#     if request.method == 'GET':
#         context = {
#             'report': report,
#             'form': ReportCreateForm(instance=report),
#         }
#         return render(request, 'actions/edit.html', context)
#     else:
#         form = ReportCreateForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         context = {
#             'report': report,
#             'form': form,
#         }
#         return render(request, 'actions/edit.html', context)

class ReportEditView(UpdateView):
    model = Report
    template_name = 'actions/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
    #TODO: add different groups maybe?
    #groups = ['Regular_Users']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'actions/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

# Add to be member of specific group
# def delete_report(request, pk):
#     report = Report.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'report': report,
#             'form': ReportDeleteForm(instance=report),
#         }
#         return render(request, 'actions/delete.html', context)
#     else:
#         report.delete()
#         return redirect('index')
