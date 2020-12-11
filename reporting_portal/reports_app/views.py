from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView
from .forms import ReportCreateForm, FilterForm
from .models import Report
from django.db.models import Q


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    title = params['title'] if 'title' in params else ''
    category = params['category'] if 'category' in params else ''

    return {
        'order': order,
        'title': title,
        'category': category,
    }


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Report
    context_object_name = 'reports'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''
    contains_category = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.order_by = params['order']
        self.contains_text = params['title']
        self.contains_category = params['category']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(Q(category__icontains=self.contains_category) &
            Q(name__icontains=self.contains_text) ).order_by(order_by)

        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'title': self.contains_text,
            'category': self.contains_category
        })

        return context


class ReportCreateView(LoginRequiredMixin, FormView):
    form_class = ReportCreateForm
    template_name = 'actions/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.save()
        return super().form_valid(form)

class ReportDetailsView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'details.html'
    context_object_name = 'report'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report = context['report']
        context['heading_text'] = f'{report.name}'
        return context


class ReportEditView(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = 'actions/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.save()
        return super().form_valid(form)


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'actions/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

