# coding=utf-8
# coding = utf-8
import datetime
import time
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models.aggregates import Sum
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from basedata.models import Material,ExtraParam,Employee,Position
from host.models import HostManager

from django.core.exceptions import ValidationError 


class HostManagerAdmin(generic.BOAdmin):
    CODE_PREFIX = ''
    CODE_NUMBER_WIDTH = 3
    list_display = ['code', 'begin_time','end_time', 'phy_host','orders','title']
    list_display_links = ['code','title']
    raw_id_fields = ['phy_host','parent']
    fieldsets = [
        (None,{'fields':[('phy_host', 'orders'),
                         ('begin_time','end_time'),
                         ('title'),
                         ('description'),
                         ]})
    ]
    
    def save_model(self, request, obj, form, change):
        timeList = HostManager.objects.all().values_list('begin_time','end_time')
        curruntBegin = time.mktime(time.strptime('%s %s' \
                        % (request.POST.get("begin_time_0"), \
                        request.POST.get("begin_time_1")),\
                        '%Y-%m-%d %H:%M:%S'))
        curruntEnd = time.mktime(time.strptime('%s %s' \
                        % (request.POST.get("end_time_0"), \
                        request.POST.get("end_time_1")),\
                        '%Y-%m-%d %H:%M:%S'))
        flag = True
        if curruntEnd <= curruntBegin:
            self.message_user(request,'ERROR:end time > begin time.',level=messages.ERROR) 
            flag = False
        for datetime in timeList:
            temp_datetime0 = datetime[0]
            temp_datetime1 = datetime[1]
            tempBegin = time.mktime(time.strptime(str(temp_datetime0),'%Y-%m-%d %H:%M:%S'))
            tempEnd = time.mktime(time.strptime(str(temp_datetime1),'%Y-%m-%d %H:%M:%S'))
            
            if (tempBegin < curruntBegin) and (tempEnd > curruntBegin):
                self.message_user(request,'ERROR:The host has been used.',level=messages.ERROR)
                flag = False
            elif (tempBegin < curruntEnd) and (tempEnd > curruntEnd):
                self.message_user(request,'ERROR:The host has been used.',level=messages.ERROR)
                flag = False
            elif (tempBegin > curruntBegin) and (tempEnd < curruntEnd):
                self.message_user(request,'ERROR:The host has been used.',level=messages.ERROR)
                flag = False
	   
        if flag:     
            super(HostManagerAdmin,self).save_model(request,obj,form,change)

    def get_changeform_initial_data(self, request):
        now = datetime.datetime.now()
        begin = now + datetime.timedelta(hours=12)
        end = begin + datetime.timedelta(hours=6)
        return {'begin_time':begin,'end_time':end}

admin.site.register(HostManager,HostManagerAdmin)
