#!/usr/bin/python

import requests


################################
#
# nlp service
#
class NlpService:
    """
    The NLP service for querying the NLP REST API
    """
    def __init__(self, url_endpoint):
        """
        :param url_endpoint: the full url endpoint to query
        """
        assert url_endpoint is not None and len(url_endpoint) > 0
        self.url_endpoint = url_endpoint

    def query(self, text, metadata={}, application_params={}):
        """
        Sends the document to the NLP service to receive back the annotations
        :param text: the text to be processed
        :param metadata: metadata fields to be included with the response
        :param application_params: application parameters
        :return: returns the full NLP service response
        """
        query_body = {
            "content": {
                "text": text
            },
            "application_params": application_params,
            "footer": metadata
        }
        response = requests.post(self.url_endpoint, json=query_body)

        # TODO: error handling
        assert response.ok
        assert 'result' in response.json()

        return response.json()


################################
#
# bioyodie service
#
class BioyodieService(NlpService):
    """
    The NLP BioYodie service
    """
    def __init__(self, url_endpoint):
        """
        :param url_endpoint: the full url endpoint to query
        """
        super().__init__(url_endpoint)

    def query(self, text, metadata={}, application_params={'annotationSets': "Bio:*"}):
        """
        Sends the document to the NLP service to receive back the annotations
        :param text: the text to be processed
        :param metadata: metadata fields to be included with the response
        :param application_params: the NLP application runtime params
        :return: returns the full NLP service response
        """
        return super().query(text, metadata, application_params)