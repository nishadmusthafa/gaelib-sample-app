
from gaelib.tests.base import BaseAuthenticatedUnitTestCase
from main import app


class BaseSampleAppTestCase(BaseAuthenticatedUnitTestCase):
  app_for_test = app

  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()
