from izug.refegovservice import _
from izug.refegovservice.config import PROJECTNAME
from izug.refegovservice.interfaces import IEgovLeistung
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from zope.interface import implements


schema = atapi.Schema((
    atapi.TextField(
        name='description',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'description'),
        )
    ),

    atapi.TextField(
        name='generalinformation',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'generalinformation'),
        )
    ),

    atapi.TextField(
        name='result',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'result'),
        )
    ),

    atapi.TextField(
        name='cost',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'cost'),
        )
    ),

    atapi.TextField(
        name='annotations',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'annotations'),
        )
    ),

    atapi.TextField(
        name='precondition',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'precondition'),
        )
    ),

    atapi.TextField(
        name='procedure',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'procedure'),
        )
    ),


    atapi.TextField(
        name='forms',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'forms'),
        )
    ),

    atapi.TextField(
        name='requireddocuments',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'requireddocuments'),
        )
    ),


    atapi.TextField(
        name='legalbases',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'legalbases'),
        )
    ),


    atapi.TextField(
        name='additionalinformation',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            rows=4,
            label=_(u'additionalinformation'),
        )
    ),

    atapi.TextField(
        name='address',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html', ),
        default_content_type='text/html',
        validators=('isTidyHtmlWithCleanup', ),
        default_input_type='text/html',
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'address'),
            rows=5,
        ),
    ),

),
)


EgovLeistungSchema = schemata.ATContentTypeSchema.copy() + schema.copy()
schemata.finalizeATCTSchema(EgovLeistungSchema, folderish=0)


class EgovLeistung(ATCTContent):
    """
    """

    schema = EgovLeistungSchema

    implements(IEgovLeistung)


atapi.registerType(EgovLeistung, PROJECTNAME)
