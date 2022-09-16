"""
    This module contains the api view classes for the
    Sample Entity API.
"""
from controllers.sample_model_controller import SampleModelController
from gaelib.view.base_view import BaseAPIHandler

class SampleEntities(BaseAPIHandler):
  controller = SampleModelController

class SampleEntity(BaseAPIHandler):
  controller = SampleModelController

