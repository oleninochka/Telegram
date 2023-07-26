from app.handler.router.auth import authenticated_router, unauthenticated_router


def register_routes():
    unauthenticated_router()
    authenticated_router()
