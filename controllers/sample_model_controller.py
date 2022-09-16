"""
    This module defines the database controller for SampleModel kind.
"""
from models.sample_model import SampleModel


class SampleModelController():
  """
      The controller for the Sample Model
  """
  @staticmethod
  def get_entities(entity_id=None):
    kwargs = {}
    if entity_id:
      kwargs = {'key_strs': [entity_id]}
    return SampleModel.retrieve(**kwargs)

  @staticmethod
  def validate_fields(**kwargs):
    # perform validation here
    return True, None

  @staticmethod
  def create_or_update_entity(sample_entity_id='', **kwargs):
    if sample_entity_id:
      sample_entity = SampleModel(key_str=sample_entity_id)
    else:
      sample_entity = SampleModel()

    validated, errors = SampleModelController.validate_fields(**kwargs)
    if validated:
      sample_entity.update(string_field=kwargs.get('string_field'),
                           date_field=kwargs.get('date_field'),
                           #  needs validation
                           float_field=kwargs.get('float_field'),
                           )
      sample_entity.put()
    return sample_entity, errors

  @staticmethod
  def delete_entity(sample_entity_id):
    sample_entity = SampleModel(key_str=sample_entity_id)
    sample_entity.delete()
