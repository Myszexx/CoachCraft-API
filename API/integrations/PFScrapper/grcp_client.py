import json
import grpc
from API.integrations.PFScrapper.scraper_pb2_grpc import ScraperServiceStub
from API.integrations.PFScrapper.scraper_pb2 import ScraperRequest

class GRPCClient:
    def __init__(self, config_file='API/integr_settings.json'):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.host = config['PFScrapper'].get('grpc_host', 'localhost')
        self.port = config['PFScrapper'].get('grpc_port', 50051)
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = ScraperServiceStub(self.channel)

    def get_data(self, request_data):
        request = ScraperRequest(url=request_data)
        response = self.stub.GetNinetyZPNs(request)
        return response