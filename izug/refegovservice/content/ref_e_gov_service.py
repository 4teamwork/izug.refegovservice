# -*- coding: utf-8 -*-
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from z3c.relationfield import RelationChoice
from zope import schema
from zope.interface import implementer

from plone.app.dexterity import MessageFactory as DXMF
from izug.refegovservice import _


class IRefEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for RefEGovService
    """

    # Copy title from IBasic behavior. We don't want description
    title = schema.TextLine(
        title=DXMF(u'label_title', default=u'Title'),
        required=True
    )

    directives.order_before(title='*')

    directives.omitted('title')
    directives.no_omit(IEditForm, 'title')
    directives.no_omit(IAddForm, 'title')

    referencedService = RelationChoice(
        title=_(u'referencedService'),
        required=False,
        source=ObjPathSourceBinder(
            portal_type=['izug.refegovservice.egovservice']
        )
        # TODO may need to set Widget properties as below
        # widget=ReferenceBrowserWidget(
        #     label='Service Referenz',
        #     default_search_index='Title'
        # ),
    )


@implementer(IRefEGovService)
class RefEGovService(Item):
    """
    """
