# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield import RelationChoice
from zope.interface import implementer

from izug.refegovservice import _


class IRefEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for RefEGovService
    """

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
