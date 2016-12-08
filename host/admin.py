# coding=utf-8
# coding = utf-8
import datetime
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models.aggregates import Sum
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from basedata.models import Material,ExtraParam,Employee,Position
from host.models import HostManager


class HostManagerAdmin(generic.BOAdmin):
    CODE_PREFIX = 'AC'
    CODE_NUMBER_WIDTH = 5
    list_display = ['code','phy_host', 'begin_time','end_time','orders','title']
    list_display_links = ['code','title']
    raw_id_fields = ['phy_host','parent']
    fieldsets = [
        (None,{'fields':[('phy_host', 'orders'),
                         ('begin_time','end_time'),
                         ('title'),
                         ('description'),
                         ]})
    ]

    def get_changeform_initial_data(self, request):
        now = datetime.datetime.now()
        begin = now + datetime.timedelta(hours=12)
        end = begin + datetime.timedelta(hours=6)
        return {'begin_time':begin,'end_time':end}

admin.site.register(HostManager,HostManagerAdmin)
