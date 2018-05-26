from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from auction_bid.utils import FlaskCelery
from service_modules.flask_jwt_parser import JWTParser
from service_modules.i18n import init_babel
from service_modules.kvd_flask import KVDFlask
from service_modules.service_discovery import ServiceCall

db = SQLAlchemy()
celery_app = FlaskCelery(__name__)
service_call = ServiceCall()


def create_app(config_file='appconf.json', register_service=False) -> KVDFlask:
    """
    Create the flask application. By default a configuration file called "defaultconf.json" is loaded.
    This can be overridden by the config file given as a parameter to this function.
    :param config_file: The json-formatted configuration file used to override the default configuration.
    :param register_service: Create SRV record for the service
    """
    app = KVDFlask(__name__)
    app.config.from_json(config_file)
    app.init_logging()

    # Importing models so SQLAlchemy is aware of them
    from auction_bid import models  # NOQA

    from auction_bid import tasks  # NOQA
    celery_app.init_app(app)

    # For now, we are setting the registry on the app,
    # we will most likely want to refactor this in the future.
    # This enables us to use current_app.service_registry in our Resource files
    if register_service:
        app.register_service()

    # Creating api here because of a bug which causes tests to not clean up properly if defined
    # in global scope
    api = Api(app)
    JWTParser(app)
    db.init_app(app)
    add_api_resources(api)
    init_babel(app)

    return app


def add_api_resources(api: Api):
    """
    Add resources needed by the microservice here.
    """
    from auction_bid import resources
    api.add_resource(resources.MemberAuctionInformation, '/v1/auctions/<string:auction_id>/me')
    api.add_resource(resources.MemberAuctionInformationList, '/v1/auctions/me')
    api.add_resource(resources.MaxBidList, '/v1/auctions/<string:auction_id>/max-bids')
    api.add_resource(resources.MaxBid, '/v1/auctions/<string:auction_id>/max-bids/<string:max_bid_id>')
    api.add_resource(resources.MaxBidByIds, '/v1/auctions/max-bids/by_ids')
    api.add_resource(resources.BidList, '/v1/auctions/<string:auction_id>/bids')
    api.add_resource(resources.Bid, '/v1/auctions/<string:auction_id>/bids/<string:bid_id>')
    api.add_resource(resources.ActiveAuctionList, '/v1/auctions')
    api.add_resource(resources.ActiveAuction, '/v1/auctions/<string:auction_id>')
    api.add_resource(resources.ActiveAuctionAbort, '/v1/auctions/<string:auction_id>/abort')
    api.add_resource(resources.ActiveAuctionStatistics, '/v1/auction_statistics')
    api.add_resource(resources.TonightStatistics, '/v1/tonight_statistics')
    api.add_resource(resources.ActiveAuctionListByIds, '/v1/auctions/by_ids')
