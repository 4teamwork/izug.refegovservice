import unittest2 as unittest
from izug.refegovservice.testing import IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING
from Products.CMFCore.utils import getToolByName
from izug.refegovservice.interfaces import IRevEgovConfig


class TestIntegration(unittest.TestCase):

    layer = IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.portal.invokeFactory('Folder', 'f1')
        self.folder = self.portal['f1']

    def test_service(self):
        """test the service"""
        data = dict(
            eCHserviceID="00488",
            eCHlanguageID="DE",
            eCHmunicipalityID="01711",
            eCHserviceVersionID="13421")
        self.folder.invokeFactory('RefEgovService', 's1', **data)
        service = self.folder['s1']
        service_view = service.restrictedTraverse('refegovservice_view')
        self.assertTrue(isinstance(service_view.get_body(), dict))

    def test_invalid_url_cache(self):
        """
        test the service with an invalid url. the value stored in the cache
        will be returned.
        """
        pt = getToolByName(self.folder, 'portal_properties')
        pt.wsrefegov_property_sheet.client_url = u'http://localhost:8888'
        data = dict(
            eCHserviceID="00488",
            eCHlanguageID="DE",
            eCHmunicipalityID="01711",
            eCHserviceVersionID="13421")
        self.folder.invokeFactory('RefEgovService', 's1', **data)
        service = self.folder['s1']
        # set a cache
        config = IRevEgovConfig(service)
        config.set_ref_ch_cache('test', 'test cache')
        service_view = service.restrictedTraverse('refegovservice_view')
        self.assertTrue(service_view.get_response() == 'test cache')

    def test_invalid_url_no_cache(self):
        """
        test the service with an invalid url.
        """
        pt = getToolByName(self.folder, 'portal_properties')
        pt.wsrefegov_property_sheet.client_url = u'http://localhost:8888'
        data = dict(
            eCHserviceID="00488",
            eCHlanguageID="DE",
            eCHmunicipalityID="01711",
            eCHserviceVersionID="13421")
        self.folder.invokeFactory('RefEgovService', 's1', **data)
        service = self.folder['s1']
        service_view = service.restrictedTraverse('refegovservice_view')
        self.assertEquals(service_view.get_body(), {})

    def test_no_wsdl(self):
        """
        test the service with an url with no wsdl.
        """
        pt = getToolByName(self.folder, 'portal_properties')
        pt.wsrefegov_property_sheet.client_url = self.portal.absolute_url()
        data = dict(
            eCHserviceID="00488",
            eCHlanguageID="DE",
            eCHmunicipalityID="01711",
            eCHserviceVersionID="13421")
        self.folder.invokeFactory('RefEgovService', 's1', **data)
        service = self.folder['s1']
        service_view = service.restrictedTraverse('refegovservice_view')
        self.assertTrue(service_view.get_body() == {})
