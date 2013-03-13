from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import setRoles, TEST_USER_ID, TEST_USER_NAME, login
from plone.testing import z2
from zope.configuration import xmlconfig


class RefeGovServiceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import izug.refegovservice
        xmlconfig.file('configure.zcml', izug.refegovservice,
                       context=configurationContext)

        # installProduct() is *only* necessary for packages outside
        # the Products.* namespace which are also declared as Zope 2
        # products, using <five:registerPackage /> in ZCML.
        z2.installProduct(app, 'izug.refegovservice')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'izug.refegovservice:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)


IZUG_REFEGOVSERVICE_FIXTURE = RefeGovServiceLayer()
IZUG_REFEGOVSERVICE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IZUG_REFEGOVSERVICE_FIXTURE, ),
    name="IzugRefEgovService:Integration")
IZUG_REFEGOVSERVICE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IZUG_REFEGOVSERVICE_FIXTURE, ),
    name="IzugRefEgovService:Functional")
