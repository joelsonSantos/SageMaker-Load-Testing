from locust import HttpUser, task
from authorizer import authorize
import config as conf
import json
from mock_data import MockData

# For content type=application/json use similar to below 2 lines
PAYLOAD = MockData().model_data()
PAYLOAD = json.dumps(PAYLOAD)


class WebsiteUser(HttpUser):
    min_wait = 1
    max_wait = 5  # time in ms

    @task
    def test_post(self):
        """
        Load Test SageMaker Endpoint (POST request)
        """
        headers = authorize(PAYLOAD)
        headers['X-Amz-Security-Token'] = conf.SESSION_KEY
        self.client.post(conf.SAGEMAKER_ENDPOINT_URL, data=PAYLOAD, headers=headers, name='Post Request')
