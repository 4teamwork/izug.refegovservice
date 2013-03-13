from zope.interface import Interface


class IRefEgovService(Interface):
    """Marker interfaces for refegovservice"""


class IRevEgovConfig(Interface):
    """RefEgovService configuration"""

    def __init__(context):
        """Adapts context"""

    def get_ref_ch_cache():
        """
        Returns the ref_ch_cache dict (md5, response) form annotations
        """

    def set_ref_ch_cache(md5_hash, response):
        """
        Saves the new md5_hash and the response into the ref_ch_cache
        annotation
        """
