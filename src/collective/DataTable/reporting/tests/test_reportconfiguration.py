# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.DataTable.reporting.testing import COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING  # noqa
from collective.DataTable.reporting.interfaces import IReportConfiguration

import unittest2 as unittest


class ReportConfigurationIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='ReportConfiguration')
        schema = fti.lookupSchema()
        self.assertEqual(IReportConfiguration, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='ReportConfiguration')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='ReportConfiguration')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IReportConfiguration.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('ReportConfiguration', 'ReportConfiguration')
        self.assertTrue(
            IReportConfiguration.providedBy(self.portal['ReportConfiguration'])
        )
