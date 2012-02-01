import webapp2

from collections import OrderedDict


STATUS_CODES_DESCRIPTION_URL = 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html'


STATUS_CODES =  OrderedDict([
    ('1xx', 'Informational'),
    ('100', 'Continue'),
    ('101', 'Switching Protocols'),

    ('2xx', 'Successful'), 
    ('200', 'OK'),
    ('201', 'Created'),
    ('202', 'Accepted'),
    ('203', 'Non-Authoritative Information'),
    ('204', 'No Content'),
    ('205', 'Reset Content'),
    ('206', 'Partial Content'),

    ('3xx', 'Redirection'),
    ('300', 'Multiple Choices'),
    ('301', 'Moved Permanently'),
    ('302', 'Found'),
    ('303', 'See Other'),
    ('304', 'Not Modified'),
    ('305', 'Use Proxy'),
    ('306', '(Unused)'),
    ('307', 'Temporary Redirect'),

    ('4xx', 'Client Error'),
    ('400', 'Bad Request'),
    ('401', 'Unauthorized'),
    ('402', 'Payment Required'),
    ('403', 'Forbidden'),
    ('404', 'Not Found'),
    ('405', 'Method Not Allowed'),
    ('406', 'Not Acceptable'),
    ('407', 'Proxy Authentication Required'),
    ('408', 'Request Timeout'),
    ('409', 'Conflict'),
    ('410', 'Gone'),
    ('411', 'Length Required'),
    ('412', 'Precondition Failed'),
    ('413', 'Request Entity Too Large'),
    ('414', 'Request-URI Too Long'),
    ('415', 'Unsupported Media Type'),
    ('416', 'Requested Range Not Satisfiable'),
    ('417', 'Expectation Failed'),

    ('5xx', 'Server Error'),
    ('500', 'Internal Server Error'),
    ('501', 'Not Implemented'),
    ('502', 'Bad Gateway'),
    ('503', 'Service Unavailable'),
    ('504', 'Gateway Timeout'),
    ('505', 'HTTP Version Not Supported'),
])


class MainPage(webapp2.RequestHandler):
    def get(self, code=None):
        self.response.headers['Content-Type'] = 'text/plain'
        if code:
            self.response.status = code
            self.response.out.write('%s %s\n' % (code, STATUS_CODES[code]))
        else:
            for code in STATUS_CODES:
                if 'x' in code and code!='1xx':
                    self.response.out.write('\n\n')
                self.response.out.write('%s %s\n' % (code, STATUS_CODES[code]))
                if 'x' in code:
                    self.response.out.write('\n')
        self.response.out.write('\n\nMore information about status codes can be found at %s' %
                                STATUS_CODES_DESCRIPTION_URL)

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/(\d{3})?/?', MainPage)],
                              debug=True)