"""
    This module defines the database model for SampleModel kind.
"""
from gaelib.db import model, properties


class SampleModel(model.Model):
  """
      The database model for a Sample Entity
  """
  string_field = properties.StringProperty()
  date_field = properties.DateTimeProperty()
  float_field = properties.FloatProperty()

  def to_json(self):
    return {'string_field': self.string_field,
            'date_field': self.date_field,
            'float_field': self.float_field
            }
