from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from izug.refegovservice.testing import IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from unittest2 import TestCase


class TestCreation(TestCase):

    layer = IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING

    def setUp(self):
        super(TestCreation, self).setUp()

        self.portal = self.layer['portal']
        self.portal_url = self.portal.portal_url()

        self.leistung = create(Builder('egov leistung')
                               .titled('Leistung')
                               .having(description='The Description',
                                       generalinformation='Some infos',
                                       result='A result'))

        self.refservice = create(Builder('ref egov service')
                                 .titled('Reference')
                                 .having(referencedService=self.leistung))

    def test_fti(self):
        self.assertIn('RefEgovService', self.portal.portal_types.objectIds())
        self.assertIn('EgovLeistung', self.portal.portal_types.objectIds())

    @browsing
    def test_description_is_not_rendered(self, browser):
        browser.login().visit(self.refservice)
        self.assertNotIn('The Description',
                         browser.css('h2'),
                         'Description should no be rendered.')

    @browsing
    def test_creation_render(self, browser):
        browser.login(TEST_USER_NAME, TEST_USER_PASSWORD)

        browser.visit(self.refservice)

        self.assertEquals('Leistung',
                          browser.css('.documentFirstHeading').first.text)

        fields = browser.css('h2')
        self.assertIn('A result',
                      fields.pop().parent().text)

        self.assertIn('Some infos',
                      fields.pop().parent().text)
