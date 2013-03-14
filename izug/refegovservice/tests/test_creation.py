from unittest2 import TestCase
from izug.refegovservice.testing import IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING
from plone.testing.z2 import Browser
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from pyquery import PyQuery


class TestCreation(TestCase):

    layer = IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING

    def setUp(self):
        super(TestCreation, self).setUp()

        self.portal = self.layer['portal']
        self.portal_url = self.portal.portal_url()

        # Browser setup
        self.browser = Browser(self.layer['app'])
        self.browser.handleErrors = False

        self.browser.addHeader('Authorization', 'Basic %s:%s' % (
                TEST_USER_NAME, TEST_USER_PASSWORD, ))

    def tearDown(self):
        super(TestCreation, self).tearDown()

    def test_fti(self):
        self.assertIn('RefEgovService', self.portal.portal_types.objectIds())

    def test_creation_render(self):
        _id = self.portal.invokeFactory('RefEgovService', 'service')
        self.assertIn(_id, self.portal.objectIds())

        self.browser.open('%s/createObject?type_name=RefEgovService' %
            self.portal_url)
        self.browser.getControl("Title").value = 'New Service'
        self.browser.getControl("eCHserviceID").value = '00488'
        self.browser.getControl("eCHserviceVersionID").value = '13421'
        self.browser.getControl("Save").click()
        self.assertEquals(self.browser.url,
                          "%s/new-service" % self.portal_url)

        pq = PyQuery(self.browser.contents)

        self.assertTrue(pq('#content .documentFirstHeading'))
        self.assertTrue(len(pq('#content h2')) > 1, 'Expect some h2 tags')
        self.assertTrue(len(pq('#content p')) > 1, 'Expect some p tags')
        self.assertTrue('No service found' not in self.browser.contents)
