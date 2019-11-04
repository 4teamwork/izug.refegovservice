# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from z3c.relationfield import RelationChoice
from zope import schema
from zope.interface import implementer

from plone.app.dexterity import MessageFactory as DXMF
from izug.refegovservice import _


class IEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for EGovService
    """
    # Copy IBasic behavior to change description title to 'description'!
    title = schema.TextLine(
        title=DXMF(u'label_title', default=u'Title'),
        required=True
    )

    description = schema.Text(
        title=DXMF(u'label_description', default=u'Description'),
        description=DXMF(
            u'help_description',
            default=u'Used in item listings and search results.'
        ),
        required=False,
        missing_value=u'',
    )

    form.order_before(description='*')
    form.order_before(title='*')

    form.omitted('title', 'description')
    form.no_omit(IEditForm, 'title', 'description')
    form.no_omit(IAddForm, 'title', 'description')

    form.widget('summary', RichTextWidget, rows=5)
    summary = RichText(
        title=_(u'summary', default=u'Summary'),
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
        title=_(u'orgunit', default=u'OrgUnit'),
        required=False,
        source=ObjPathSourceBinder()
    )


@implementer(IEGovService)
class EGovService(Item):
    """
    """
