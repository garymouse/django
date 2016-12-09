#oding=utf-8
import datetime
import os
import xlrd
import decimal
from django.db import transaction
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import force_text
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from mis import settings
from basedata.models import Material,ExtraParam,Project,ExpenseAccount,Measure
from organ.models import OrgUnit


class HostManager(generic.BO):
    """

    """
    #CLASSIFICATION = (
    #    ('T',_("Train")),
    #    ('M',_("Meeting")),
    #    ('G',_("Community")),
    #)
    index_index_weight = 4
    begin_time = models.DateTimeField(_('begin time'))
    end_time = models.DateTimeField(_('end time'))
    #enroll_deadline = models.DateTimeField(_('enroll deadline'),blank=True,null=True)
    code = models.CharField(_("code"),max_length=const.DB_CHAR_NAME_20,blank=True,null=True)
    title = models.CharField(_("title"),max_length=const.DB_CHAR_NAME_120)
    parent = models.ForeignKey('self',verbose_name=_("parent"),blank=True,null=True)
    description = models.TextField(_("description"),blank=True,null=True)
    orders = models.CharField(_("orders"),max_length=const.DB_CHAR_NAME_80,blank=True,null=True)
    #speaker = models.CharField(_("speaker"),max_length=const.DB_CHAR_NAME_80,blank=True,null=True)
    #accept_enroll = models.BooleanField(_("accept enroll"),default=1)
    phy_host = models.ForeignKey(Material,verbose_name=_("phy_host"),blank=True,null=True,limit_choices_to={'tp':99})
    #location = models.CharField(_("location"),max_length=const.DB_CHAR_NAME_80,blank=True,null=True)
    #classification = models.CharField(_("classification"),max_length=const.DB_CHAR_CODE_2,blank=True,null=True,choices=CLASSIFICATION,default='M')
    #mail_list = models.TextField(_("mail list"),blank=True,null=True)
    #mail_notice = models.BooleanField(_("mail notice"),default=1)
    #short_message_notice = models.BooleanField(_("short message notice"),default=1)
    #weixin_notice = models.BooleanField(_("weixin notice"),default=1)
    #status = models.BooleanField(_("published"),default=0)
    #publish_time = models.DateTimeField(_("publish time"),blank=True,null=True)
    #attach = models.FileField(_("attach"),blank=True,null=True,upload_to='host')

    class Meta:
        verbose_name = _("order host")
        verbose_name_plural = _("hosts")

