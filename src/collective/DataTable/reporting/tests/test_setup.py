# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.DataTable.reporting.testing import COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.DataTable.reporting is properly installed."""

    layer = COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.DataTable.reporting is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.DataTable.reporting'))

    def test_browserlayer(self):
        """Test that ICollectiveDatatableReportingLayer is registered."""
        from collective.DataTable.reporting.interfaces import (
            ICollectiveDatatableReportingLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveDatatableReportingLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DATATABLE_REPORTING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.DataTable.reporting'])

    def test_product_uninstalled(self):
        """Test if collective.DataTable.reporting is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.DataTable.reporting'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveDatatableReportingLayer is removed."""
        from collective.DataTable.reporting.interfaces import ICollectiveDatatableReportingLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveDatatableReportingLayer, utils.registered_layers())
