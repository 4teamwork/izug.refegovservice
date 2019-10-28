# -*- coding: utf-8 -*-
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.app.vocabularies.catalog import CatalogSource
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from z3c.relationfield import RelationChoice
from zope import schema
from zope.interface import implementer

from plone.app.dexterity import MessageFactory as PLONE_APP_DX_MF
from izug.refegovservice import _

import six


class IRefEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for RefEGovService
    """

    # Copy title from IBasic behavior. We don't want description
    title = schema.TextLine(
        title=PLONE_APP_DX_MF(u'label_title', default=u'Title'),
        required=True
    )

    directives.order_before(title='*')

    directives.omitted('title')
    directives.no_omit(IEditForm, 'title')
    directives.no_omit(IAddForm, 'title')

    referencedService = RelationChoice(
        title=_(u'referencedService'),
        required=False,
        source=CatalogSource(portal_type=['izug.egovservice'])
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
    # copied from metadata.Basic
    def _get_title(self):
        return self.context.title

    def _set_title(self, value):
        if not isinstance(value, six.text_type):
            raise ValueError('Title must be text.')
        self.context.title = value
    title = property(_get_title, _set_title)
