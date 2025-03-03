import json
import grpc
from API.integrations.PFScrapper.scraper_pb2_grpc import ScraperServiceStub
from  API.integrations.PFScrapper.scraper_pb2 import ScraperRequest

GRPC_SERVER_ADDRESS = "grpc_server:50051"

def get_ninety_teams(url):
    """Funkcja wywołująca scraper przez gRPC."""
    with grpc.insecure_channel(GRPC_SERVER_ADDRESS) as channel:
        stub = ScraperServiceStub(channel)
        request = ScraperRequest(url=url)
        response = stub.GetNinetyTeams(request)
    return response.data
