from zope.deprecation import deprecated
from zope.interface import Interface


class IRefEGovService(Interface):
    """Marker interfaces for refegovservice"""


class IEGovService(Interface):
    """Marker interfaces for refegovservice"""


# Old names for these interfaces - probably unused, but deprecated to make sure
IEgovLeistung = IRefEGovService
IRefEgovService = IRefEGovService

deprecated(
    ['IEgovLeistung'],
    'Marker interface has been deprecated in favour of new dexterity schema '
    'izug.refegovservice.content.e_gov_service.IEGovService'
    ''
)
deprecated(
    ['IRefEgovService'],
    'Marker interface has been deprecated in favour of new dexterity schema '
    'izug.refegovservice.content.ref_e_gov_service.IRefEGovService'
)
