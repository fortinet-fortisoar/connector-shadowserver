"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""
import requests
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('shadowserver')


class ShadowServer(object):

    def __init__(self, config):
        self.server_url = config.get('server_url','').strip()
        self.headers = {'accept': 'application/json'}
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False):
        url = self.server_url + endpoint
        logger.debug('API Service Endpoint: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def get_origin_query(config, params):
    """
    Report back the originating ASN and ASN name for the specific CIDR.
    :param config: config
    :param params: params
    :return:Report back the originating ASN and ASN name for the specific CIDR.
    """
    obj = ShadowServer(config)
    endpoint = '/net/asn?origin={0}'.format(params.get('ip_address'))
    return obj.make_api_call(endpoint=endpoint)

def get_peer_query(config, params):
    """
     Report back all the BGP peers for a specific CIDR.
    :param config: config
    :param params: params
     Report back all the BGP peers for a specific CIDR.
    """
    obj = ShadowServer(config)
    endpoint = '/net/asn?peer={0}'.format(params.get('ip_address'))
    return obj.make_api_call(endpoint=endpoint)

def get_prefix_query(config, params):
    """
     Given an ASN report back all the routed CIDR's.
    :param config: config
    :param params: params
     Given an ASN report back all the routed CIDR's.
    """
    obj = ShadowServer(config)
    endpoint = '/net/asn?prefix={0}'.format(params.get('query'))
    return obj.make_api_call(endpoint=endpoint)

def get_asn_query(config, params):
    """
     Report back any information about the ASN.
    :param config: config
    :param params: params
     Report back any information about the ASN.
    """
    obj = ShadowServer(config)
    endpoint = '/net/asn?query={0}'.format(params.get('query'))
    return obj.make_api_call(endpoint=endpoint)

def get_malware_query(config, params):
    """
     Returns a JSON response containing static details about the requested sample as well as antivirus vendor and signature details.
    :param config: config
    :param params: params
    Returns a JSON response containing static details about the requested sample as well as antivirus vendor and signature details.
    """
    obj = ShadowServer(config)
    endpoint = '/malware/info?sample={0}'.format(params.get('md5'))
    return obj.make_api_call(endpoint=endpoint)

def get_programs_query(config, params):
    """
     Report back any information about the ASN.
    :param config: config
    :param params: params
     Report back any information about the ASN.
    """
    obj = ShadowServer(config)
    endpoint = '/program/trusted?sample={0}'.format(params.get('query'))
    return obj.make_api_call(endpoint=endpoint)

def _check_health(config):
    try:
        obj = ShadowServer(config)
        obj.make_api_call(endpoint='/net/asn?origin=8.8.8.8', health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


operations = {
    'get_origin_query': get_origin_query,
    'get_peer_query': get_peer_query,
    'get_prefix_query': get_prefix_query,
    'get_asn_query': get_asn_query,
    'get_malware_query': get_malware_query,
    'get_programs_query': get_programs_query
}
