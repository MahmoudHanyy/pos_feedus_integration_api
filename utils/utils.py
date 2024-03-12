import re 

def get_active_db(request):
    SYS_PARAMS = request.env['ir.config_parameter'].sudo()
    web_base_url = SYS_PARAMS.search([
        ('key','=','web.base.url')
    ], limit=1).value
    domain = re.search('https?://([A-Za-z_0-9.-]+).*', web_base_url)
    return request.session.db or domain.group(1)