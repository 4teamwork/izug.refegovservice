# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.relationfield import RelationChoice
from zope.interface import implementer

from izug.refegovservice import _


class IEGovService(model.Schema):
    """ Marker interface and Dexterity Python Schema for EGovService
    """

    summary = RichText(
        title=_(u'summary'),
        required=False
    )

    generalinformation = RichText(
        title=_(u'generalinformation'),
        required=False
    )

    precondition = RichText(
        title=_(u'precondition'),
        required=False
    )

    procedure = RichText(
        title=_(u'procedure'),
        required=False
    )

    forms = RichText(
        title=_(u'forms'),
        required=False
    )

    requireddocuments = RichText(
        title=_(u'requireddocuments'),
        required=False
    )

    result = RichText(
        title=_(u'result'),
        required=False
    )

    cost = RichText(
        title=_(u'cost'),
        required=False
    )

    legalbases = RichText(
        title=_(u'legalbases'),
        required=False
    )

    additionalinformation = RichText(
        title=_(u'additionalinformation'),
        required=False
    )

    additionalinformation = RichText(
        title=_(u'additionalinformation'),
        required=False
    )

    annotations = RichText(
        title=_(u'annotations'),
        required=False
    )

    address = RichText(
        title=_(u'address'),
        required=False,
    )

    orgunit = RelationChoice(
        title=_(u'orgunit'),
        required=False,
        vocabulary='plone.app.vocabularies.Catalog'
    )

    # Used to choose language that headings are displayed in
    fieldset('Default', fields=['language'])


@implementer(IEGovService)
class EGovService(Item):
    """
    """
