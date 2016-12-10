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


class MaManager(generic.BO):
    """

    """
    index_index_weight = 4
    code = models.CharField(_("code"),max_length=const.DB_CHAR_NAME_20,blank=True,null=True)
    name = models.CharField(_("name"),max_length=const.DB_CHAR_NAME_120)
    parent = models.ForeignKey('self',verbose_name=_("parent"),blank=True,null=True)
    ip = models.CharField(_("ip"),max_length=const.DB_CHAR_NAME_120)
    detail = models.CharField(_("detail"),max_length=const.DB_CHAR_NAME_120)

    class Meta:
        verbose_name = _("order ma")
        verbose_name_plural = _("mas")

