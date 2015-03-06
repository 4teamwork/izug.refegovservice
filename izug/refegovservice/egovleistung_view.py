from ftw.table.interfaces import ITableGenerator
from izug.refegovservice import _
from Products.Five.browser import BrowserView
from zope.component import queryUtility
from zope.i18n import translate
from ftw.table.helper import readable_date_time_text
from ftw.table.helper import link


class EgovLeistungView(BrowserView):

    def translate(self, msgid):
        lang = self.context.Language()
        if not lang:
            lang = 'de'
        return translate(msgid,
                         domain='izug.refegovservice',
                         context=self.request,
                         target_language=lang)


def link_orgunit(item, value):
    orgunit = item.getObject().getOrgunit()

    if orgunit:
        return '<a href="%s" title="%s">%s</a>' % (
            orgunit.absolute_url(),
            orgunit.Description(),
            orgunit.Title())
    else:
        return ''


class EgovLeistungOverview(BrowserView):

    def render_table(self):
        generator = queryUtility(ITableGenerator, 'ftw.tablegenerator')
        return generator.generate(self.contents(),
                                  self.columns(),
                                  sortable=True,
                                  selected=('sortable_title', 'asc'),)

    def contents(self):
        return self.context.getFolderContents(
            {'portal_type': 'EgovLeistung', 'sort_on': 'sortable_title'})

    def columns(self):
        return [
            {'column': 'Title',
             'column_title': _(u'column_title', default=u'Title'),
             'sort_index': 'sortable_title',
             'transform': link(icon=False)
             },
            {'column': 'orgunit',
             'column_title': _(u'column_orgunit', default=u'OrgUnit'),
             'transform': link_orgunit
             },
            {'column': 'modified',
             'column_title': _(u'column_modified', default=u'Modified'),
             'transform': readable_date_time_text
             }
        ]
