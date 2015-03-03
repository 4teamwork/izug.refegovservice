from Products.Five.browser import BrowserView
from zope.i18n import translate


class EgovLeistungView(BrowserView):

    def translate(self, msgid):
        lang = self.context.Language()
        if not lang:
            lang = 'de'
        return translate(msgid,
                         domain='izug.refegovservice',
                         context=self.request,
                         target_language=lang)
