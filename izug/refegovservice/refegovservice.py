from Products.ATContentTypes.content import schemata
from Products.Archetypes import atapi
from Products.ATContentTypes.content.base import ATCTContent
from izug.refegovservice.config import PROJECTNAME
from izug.refegovservice import _


schema = atapi.Schema((
    atapi.StringField(
        'herausgeber',
        required=False,
        multiValued=False,
        widget=atapi.StringWidget(
            label=_(u'zugwebsite_label_author', default=u'Author'),
        ),
    ),

    atapi.StringField(
        'eCHserviceID',
        required=True,
        multiValued=False,
        widget=atapi.StringWidget(
            label=_(u'eCHserviceID', default=u'eCHserviceID'),
        ),
    ),

    atapi.StringField(
        'eCHserviceVersionID',
        required=True,
        multiValued=False,
        widget=atapi.StringWidget(
            label=_(u'eCHserviceVersionID', default=u'eCHserviceVersionID'),
        ),
    ),

    atapi.StringField(
        'eCHserviceURI',
        required=False,
        multiValued=False,
        widget=atapi.StringWidget(
            label=_(u'eCHserviceURI', default=u'eCHserviceURI'),
        ),
    ),
),
)


RefEgovServiceSchema = schemata.ATContentTypeSchema.copy() + schema.copy()
RefEgovServiceSchema['herausgeber'].widget.visible = -1
RefEgovServiceSchema['eCHserviceURI'].widget.visible = -1
schemata.finalizeATCTSchema(RefEgovServiceSchema, folderish=0)


class RefEgovService(ATCTContent):
    """
    """

    schema = RefEgovServiceSchema

atapi.registerType(RefEgovService, PROJECTNAME)
