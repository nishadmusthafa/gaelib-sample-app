"""
    This module contains the view classes for the
    admin dashboard homescreen.
"""
from datetime import datetime
from flask import redirect, request, render_template, url_for

from gaelib.dashboard.views import DashboardView
from controllers.sample_model_controller import SampleModelController


class Home(DashboardView, SampleModelController):
  """
      The view to get all the game entities
      matching the filters passed
  """

  def get(self):
    test_entities = self.get_entities()
    return render_template("dashboard/home.html",
                           test_entities=test_entities,
                           view_name='sample_entity')


class AddUpdateSampleEntity(DashboardView, SampleModelController):
  """
      The view to add/update a single Sample Entity
      with the provided arguments
  """

  methods = ['POST', 'GET']

  def get(self):
    req_args = request.args.to_dict()
    sample_entity = None

    try:
      sample_entity_id = int(req_args.get('sample_entity_id', None))
    except (ValueError, TypeError):
      sample_entity_id = None

    if sample_entity_id:
      try:
        sample_entity = SampleModelController.get_entities(sample_entity_id)[0]
      except IndexError:
        sample_entity = None

    if sample_entity and not sample_entity.retrieved():
      sample_entity = None

    return render_template('dashboard/sampleentityaddupdate.html',
                           sample_entity=sample_entity,
                           view_name='sample_entity')

  def post(self):
    data = request.form.to_dict()
    try:
      sample_entity_id = int(data.get('sample_entity_id', None))
    except (ValueError, TypeError):
      sample_entity_id = None

    if data['date_field']:
      date_field = datetime.strptime(data['date_field'],
                                     '%Y-%m-%d')
    fields = {
      'string_field': data['string_field'],
      'date_field': date_field,
      'float_field': float(data['float_field'])
    }

    sample_entity, errors = self.create_or_update_entity(
      sample_entity_id=sample_entity_id,
      **fields
    )
    if errors:
      return render_template('dashboard/sampleentityaddupdate.html',
                             sample_entity=sample_entity,
                             errors=errors,
                             view_name='sample_entity')
    else:
      return redirect(url_for('admin_dashboard.Home'))


class DeleteSampleEntity(DashboardView, SampleModelController):
  """
      The view function to delete a Sample Entity
  """

  def get(self):
    req_args = request.args.to_dict()
    sample_entity_id = int(req_args['sample_entity_id'])
    self.delete_entity(sample_entity_id)
    return redirect(url_for('admin_dashboard.Home'))
