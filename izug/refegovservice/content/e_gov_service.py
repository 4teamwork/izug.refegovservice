# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.relationfield import RelationChoice
from zope.interface import implementer

from izug.refegovservice import _


class IEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for EGovService
    """

    form.widget('summary', RichTextWidget, rows=5)
    summary = RichText(
        title=_(u'summary'),
        required=False
    )

    form.widget('generalinformation', RichTextWidget, rows=5)
    generalinformation = RichText(
        title=_(u'generalinformation'),
        required=False
    )

    form.widget('precondition', RichTextWidget, rows=5)
    precondition = RichText(
        title=_(u'precondition'),
        required=False
    )

    form.widget('procedure', RichTextWidget, rows=5)
    procedure = RichText(
        title=_(u'procedure'),
        required=False
    )

    form.widget('forms', RichTextWidget, rows=5)
    forms = RichText(
        title=_(u'forms'),
        required=False
    )

    form.widget('requireddocuments', RichTextWidget, rows=5)
    requireddocuments = RichText(
        title=_(u'requireddocuments'),
        required=False
    )

    form.widget('result', RichTextWidget, rows=5)
    result = RichText(
        title=_(u'result'),
        required=False
    )

    form.widget('cost', RichTextWidget, rows=5)
    cost = RichText(
        title=_(u'cost'),
        required=False
    )

    form.widget('legalbases', RichTextWidget, rows=5)
    legalbases = RichText(
        title=_(u'legalbases'),
        required=False
    )

    form.widget('additionalinformation', RichTextWidget, rows=5)
    additionalinformation = RichText(
        title=_(u'additionalinformation'),
        required=False
    )

    form.widget('annotations', RichTextWidget, rows=5)
    annotations = RichText(
        title=_(u'annotations'),
        required=False
    )

    form.widget('address', RichTextWidget, rows=4)
    address = RichText(
        title=_(u'address'),
        required=False,
    )

    orgunit = RelationChoice(
        title=_(u'orgunit'),
        required=False,
        source=ObjPathSourceBinder()
    )

    # FIXME (see https://stackoverflow.com/questions/31163583/moving-existing-fields-behaviors-in-dexterity?noredirect=1&lq=1)
    # Used to choose language that headings are displayed in
    # fieldset('Default', fields=['language'])    # this doesn't work


@implementer(IEGovService)
class EGovService(Item):
    """
    """
