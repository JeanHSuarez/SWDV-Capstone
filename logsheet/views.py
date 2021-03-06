from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from datetime import date
from .forms import GenerateReportForm
from django.views.generic.edit import FormView
from persons.models import Member
from django.utils import timezone
from django.views.generic import (
         ListView,
         DetailView,
         CreateView,
         UpdateView,
         DeleteView
         )
from .models import LogPost, DailyAggregator, DailyReport

<<<<<<< HEAD
class PostListView(LoginRequiredMixin,ListView):
=======
class PostListView(LoginRequiredMixin, ListView):
>>>>>>> bc139d7ff5b4eeaecf1a1c8a74d291d42d4c5cd3
    model = LogPost
    template_name ='logsheet/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'logposts'
    ordering = ['-signIn']
    paginate_by = 10

class MemberPostListView(LoginRequiredMixin, ListView):
    model = LogPost
    template_name ='logsheet/member_logposts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'logposts'
    paginate_by = 5

    def get_queryset(self):
        member = get_object_or_404(Member, firstName=self.kwargs.get('firstName'))
        return LogPost.objects.filter(member=member).order_by('-signIn')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = LogPost

class PostCreateView(LoginRequiredMixin, CreateView):
    model = LogPost
    fields= ('member',)
    success_url = '/logsheet/'

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = LogPost
    fields= ('signOut',)
    success_url = '/logsheet/'

    def form_valid(self, form):
        self.object.signOut = timezone.now()
        self.object.setDuration()
        return super().form_valid(form)
#test for current user. Might not need this or need to modify

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = LogPost
    success_url = '/logsheet/'
#test for current user. Might not need this or need to modify

#Reports Aggregators
class ReportView(LoginRequiredMixin, ListView):
    model = DailyReport
    context_object_name = 'reports'
    success_url = 'logsheet-reports'
    ordering = ['-createdAt']
    paginate_by = 10

class GenerateReportView(LoginRequiredMixin, FormView):
    template_name = 'logsheet/dailyaggregator_form.html'
    form_class = GenerateReportForm
    success_url = '/logsheet/reports/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        sumDate = form.cleaned_data.get('sumDate')
        sumDate = date.fromisoformat(sumDate)
        LogPost.generateDailyGrandTotal(sumDate.year, sumDate.month, sumDate.day)
        return super().form_valid(form)

#MemberViewClasses EXCEPT: the CreateMember function which is located in persons/view

class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    template_name ='logsheet/member_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'members'
    paginate_by = 10

class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    fields= ('ssn', 'firstName', 'middleName', 'lastName', 'diagnosis')
    success_url = '/logsheet/members/'

    def form_valid(self, form):
        return super().form_valid(form)
#test for current user. Might not need this or need to modify

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = '/logsheet/members/'

"""
class DailyMemberReportCreateView(CreateView):
    model = DailyAggregator
    fields = ('id', 'member' , 'summaryDate')
    success_url = 'logsheet-reports'

    def form_valid(self, form):
        #LogPost.generateReport(member.id, 'summaryDate')
        return super().form_valid(form)

"""



#old code as reference
"""
class PostCreateView(LoginRequiredMixin, CreateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        return super().form_valid(form)
#test for current user. Might not need this or need to modify
    def test_func(self):
        logpost = self.get_object()
        if self.request == logpost.member:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LogPost
#test for current user. Might not need this or need to modify
    def test_func(self):
        logpost = self.get_object()
        if self.request == logpost.member:
            return True
        return False
"""


"""
#This is for the TimeSheet model as it entails user to login before updated

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
"""

