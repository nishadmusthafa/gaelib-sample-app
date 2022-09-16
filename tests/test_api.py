"""
    Testing module for the contest home screen.
"""
from flask import json
from models.sample_model import SampleModel
from .base import BaseSampleAppTestCase


class SampleEntityAPITestCase(BaseSampleAppTestCase):
  """
      BaseTestClass for the Sample Entity API.
  """

  def test_get_sample_entities(self):
    self.add_user_entity(
        name='user1', email='a@b.com', uid='user1', client_user=True)

    s1 = SampleModel(string_field='s1')
    s1.put()
    s2 = SampleModel(string_field='s2')
    s2.put()
    response = self.client.get(
        '/api/sampleentity/', headers=self.auth_headers())

    self.assertEqual(response.status_code, 200)

    self.assertTrue(response.is_json)
    self.assertIn(response.json['entities'][0]['string_field'], ['s1', 's2'])
    self.assertIn(response.json['entities'][1]['string_field'], ['s1', 's2'])

  def test_create_entity(self):
    """
        Testing a fetch of single entity with id
    """
    self.add_user_entity(
        name='user1', email='a@b.com', uid='user1', client_user=True)

    response = self.client.post(
        '/api/sampleentity/',
        data=json.dumps(dict(string_field='s1')),
        headers=self.auth_headers(),
        content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's1')

    response = self.client.get(
        '/api/sampleentity/', headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertIn(response.json['entities'][0]['string_field'], 's1')

  def test_get_sample_entity(self):
    self.add_user_entity(
        name='user1', email='a@b.com', uid='user1', client_user=True)

    s1 = SampleModel(string_field='s1')
    s1.put()
    s2 = SampleModel(string_field='s2')
    s2.put()

    response = self.client.get(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertIn(response.json['string_field'], 's1')

    response = self.client.get(
        f"/api/sampleentity/{s2.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's2')

  def test_update_sample_entity(self):
    self.add_user_entity(
        name='user1', email='a@b.com', uid='user1', client_user=True)
    s1 = SampleModel(string_field='s1')
    s1.put()
    response = self.client.get(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's1')

    response = self.client.post(
        f"/api/sampleentity/{s1.key().id}/",
        data=json.dumps(dict(string_field='s2')),
        headers=self.auth_headers(),
        content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's2')

    response = self.client.get(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's2')

  def test_delete_sample_entity(self):
    self.add_user_entity(
        name='user1', email='a@b.com', uid='user1', client_user=True)
    s1 = SampleModel(string_field='s1')
    s1.put()

    response = self.client.get(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['string_field'], 's1')

    response = self.client.delete(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 200)

    response = self.client.get(
        f"/api/sampleentity/{s1.key().id}/", headers=self.auth_headers())
    self.assertEqual(response.status_code, 400)
    self.assertTrue(response.is_json)
    self.assertEqual(response.json['error_message'],
                     f"No entity with id {s1.key().id}")
