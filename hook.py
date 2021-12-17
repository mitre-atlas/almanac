from plugins.almanac.app.almanac_svc import AlmanacService

name = 'Almanac'
description = 'Use the compass to Navigate CALDERA'
address = '/plugin/almanac/gui'


async def enable(services):
    app = services.get('app_svc').application
    svc = AlmanacService(services)
    app.router.add_route('POST', '/plugin/almanac/layer', svc.generate_layer)
    app.router.add_route('POST', '/plugin/almanac/adversary', svc.create_adversary_from_layer)
    app.router.add_route('GET', '/plugin/almanac/gui', svc.splash)
