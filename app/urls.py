"""
    This module contains all the url rules for the app.
"""

# pragma pylint: disable=invalid-name

from flask import Blueprint

from gaelib.env import get_dashboard_url_prefix
from gaelib.view.base_view import LazyView

dashboard_prefix = get_dashboard_url_prefix()
admin_dashboard = Blueprint(
    'admin_dashboard', __name__,
    url_prefix='/' + dashboard_prefix + '/')
admin_dashboard.add_url_rule('', view_func=LazyView(
    'views.dashboard.home.Home',
    'dashboard_home'), methods=['GET'])
admin_dashboard.add_url_rule('/sample_entity/addupdate',
                             view_func=LazyView(
                                 'views.dashboard.home.AddUpdateSampleEntity',
                                 'dashboard_add_update_sample_entity'),
                             methods=['GET', 'POST'])
admin_dashboard.add_url_rule('/sample_entity/delete',
                             view_func=LazyView(
                                 'views.dashboard.home.DeleteSampleEntity',
                                 'dashboard_delete_sample_entity'))

sample_entity_api = Blueprint(
    'sample_entity_api', __name__,
    url_prefix='/api/sampleentity/')
sample_entity_api.add_url_rule('', view_func=LazyView(
    'views.api.sample_entity.SampleEntities', 'sample_entity_api'), methods=['GET', 'POST'])
sample_entity_api.add_url_rule('<entity_id>/', view_func=LazyView(
    'views.api.sample_entity.SampleEntity', 'sample_entity_api'), methods=['GET', 'POST', 'DELETE'])
