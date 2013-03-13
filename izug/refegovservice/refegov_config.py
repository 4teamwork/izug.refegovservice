from zope.annotation.interfaces import IAnnotations
from zope.interface import implements
from persistent.mapping import PersistentMapping
from izug.refegovservice.interfaces import IRevEgovConfig


class RevEgovConfig(object):
    """
    This class implements the IRevEgovConfig interface.
    Its used to save and get the ref_ch_cache from the annotations.
    """
    implements(IRevEgovConfig)

    def __init__(self, context):
        self.context = context

    def get_ref_ch_cache(self):
        annotations = IAnnotations(self.context)

        return annotations.get('ref_ch_cache', PersistentMapping({
            'md5': '',
            'response': None,
            }))

    def set_ref_ch_cache(self, md5_hash, response):
        annotations = IAnnotations(self.context)

        annotations['ref_ch_cache'] = PersistentMapping({
            'md5': md5_hash,
            'response': response,
            })
