# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import pkg_resources


try:
    pkg_resources.get_distribution('plone.app.relationfield')
except pkg_resources.DistributionNotFound:
    HAS_RELATIONFIELD = False
else:
    HAS_RELATIONFIELD = True


@implementer(INonInstallable)
class HiddenProfiles(object):  # pragma: no cover

    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
        return [
            u'collective.cover:testfixture',
            u'collective.cover:uninstall',
        ]


def add_relationfield_behavior():
    """Add IRelatedItems behavior to FTI."""
    from plone import api
    fti = api.portal.get_tool('portal_types')['collective.cover.content']
    fti.behaviors += ('plone.app.relationfield.behavior.IRelatedItems',)


def run_after(portal_setup):
    if HAS_RELATIONFIELD:
        add_relationfield_behavior()
