# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.DataTable.reporting


class CollectiveDatatableReportingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.DataTable.reporting)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.DataTable.reporting:default')


COLLECTIVE_DATATABLE_REPORTING_FIXTURE = CollectiveDatatableReportingLayer()


COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DATATABLE_REPORTING_FIXTURE,),
    name='CollectiveDatatableReportingLayer:IntegrationTesting'
)


COLLECTIVE_DATATABLE_REPORTING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DATATABLE_REPORTING_FIXTURE,),
    name='CollectiveDatatableReportingLayer:FunctionalTesting'
)


COLLECTIVE_DATATABLE_REPORTING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_DATATABLE_REPORTING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveDatatableReportingLayer:AcceptanceTesting'
)
