from zope.deprecation import deprecated
from zope.interface import Interface


class IRefEgovService(Interface):
    """Marker interfaces for refegovservice"""


class IEgovLeistung(Interface):
    """Marker interfaces for refegovservice"""


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
