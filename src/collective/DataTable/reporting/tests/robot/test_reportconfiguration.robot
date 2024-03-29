# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.DataTable.reporting -t test_reportconfiguration.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.DataTable.reporting.testing.COLLECTIVE_DATATABLE_REPORTING_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_reportconfiguration.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ReportConfiguration
  Given a logged-in site administrator
    and an add reportconfiguration form
   When I type 'My ReportConfiguration' into the title field
    and I submit the form
   Then a reportconfiguration with the title 'My ReportConfiguration' has been created

Scenario: As a site administrator I can view a ReportConfiguration
  Given a logged-in site administrator
    and a reportconfiguration 'My ReportConfiguration'
   When I go to the reportconfiguration view
   Then I can see the reportconfiguration title 'My ReportConfiguration'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add reportconfiguration form
  Go To  ${PLONE_URL}/++add++ReportConfiguration

a reportconfiguration 'My ReportConfiguration'
  Create content  type=ReportConfiguration  id=my-reportconfiguration  title=My ReportConfiguration


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the reportconfiguration view
  Go To  ${PLONE_URL}/my-reportconfiguration
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a reportconfiguration with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the reportconfiguration title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
