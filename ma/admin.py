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
from ma.models import MaManager


class MaManagerAdmin(generic.BOAdmin):
    CODE_PREFIX = 'PHY'
    CODE_NUMBER_WIDTH = 3
    list_display = ['id', 'code','name','ip','detail']
    list_display_links = ['code','name']
    raw_id_fields = ['parent']
    search_fields = ['code','name']
    fieldsets = [
        (None,{'fields':[('name'),
                         ('ip'),
                         ('detail'),
                         ]})
    ]

admin.site.register(MaManager,MaManagerAdmin)
