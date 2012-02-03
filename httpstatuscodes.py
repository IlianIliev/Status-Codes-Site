import webapp2

from collections import OrderedDict


STATUS_CODES_DESCRIPTION_URL = 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html'
WIKIPEDIA_CODES_DESCRIPTIONS_URL = 'http://en.wikipedia.org/wiki/List_of_HTTP_status_codes'


STATUS_CODES =  OrderedDict([
    ('1xx', 'Informational'),
    ('100', 'Continue'),
    ('101', 'Switching Protocols'),
    ('102', 'Processing (WebDAV) (RFC 2518)'),
    ('103', 'Checkpoint'),
    ('122', 'Request-URI too long'),

    ('2xx', 'Successful'), 
    ('200', 'OK'),
    ('201', 'Created'),
    ('202', 'Accepted'),
    ('203', 'Non-Authoritative Information'),
    ('204', 'No Content'),
    ('205', 'Reset Content'),
    ('206', 'Partial Content'),
    ('207', 'Multi-Status (WebDAV) (RFC 4918)'),
    ('208', 'Already Reported (WebDAV) (RFC 5842)'),
    ('226', 'IM Used (RFC 3229)'),

    ('3xx', 'Redirection'),
    ('300', 'Multiple Choices'),
    ('301', 'Moved Permanently'),
    ('302', 'Found'),
    ('303', 'See Other'),
    ('304', 'Not Modified'),
    ('305', 'Use Proxy'),
    ('306', '(Unused)'),
    ('307', 'Temporary Redirect'),
    ('308', 'Resume Incomplete'),

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
    ('418', 'I\'m a teapot (RFC 2324)'),
    ('420', 'Enhance Your Calm'),
    ('422', 'Unprocessable Entity (WebDAV) (RFC 4918)'),
    ('423', 'Locked (WebDAV) (RFC 4918)'),
    ('424', 'Failed Dependency (WebDAV) (RFC 4918)'),
    ('425', 'Unordered Collection (RFC 3648)'),
    ('426', 'Upgrade Required (RFC 2817)'),
    ('428', 'Precondition Required'),
    ('429', 'Too Many Requests'),
    ('431', 'Request Header Fields Too Large'),
    ('444', 'No Response'),
    ('449', 'Retry With'),
    ('450', 'Blocked by Windows Parental Controls'),
    ('499', 'Client Closed Request'),

    ('5xx', 'Server Error'),
    ('500', 'Internal Server Error'),
    ('501', 'Not Implemented'),
    ('502', 'Bad Gateway'),
    ('503', 'Service Unavailable'),
    ('504', 'Gateway Timeout'),
    ('505', 'HTTP Version Not Supported'),
    ('506', 'Variant Also Negotiates (RFC 2295)'),
    ('507', 'Insufficient Storage (WebDAV) (RFC 4918)'),
    ('508', 'Loop Detected (WebDAV) (RFC 5842)'),
    ('509', 'Bandwidth Limit Exceeded (Apache bw/limited extension)'),
    ('510', 'Not Extended (RFC 2774)'),
    ('511', 'Network Authentication Required'),
    ('598', 'Network read timeout error'),
    ('599', 'Network connect timeout error[25]'),
])


class MainPage(webapp2.RequestHandler):
    def get(self, code=None):
        self.response.headers['Content-Type'] = 'text/plain'
        if code:
            if code in STATUS_CODES and 'xx' not in code:
                if code.startswith('1'):
                    self.response.set_status(500, message=STATUS_CODES['500'])
                    self.response.out.write('Google App Engine does not support the status codes from the Informational Group - 1xx')
                else:
                    self.response.set_status(int(code), message=STATUS_CODES[code])
                    self.response.out.write('%s %s\n' % (code, STATUS_CODES[code]))
            else:
                self.response.set_status(404, message=STATUS_CODES['404'])
                self.response.out.write('There is no such status code as %s' % code)
        else:
            for code in STATUS_CODES:
                if 'x' in code and code!='1xx':
                    self.response.out.write('\n\n')
                self.response.out.write('%s %s\n' % (code, STATUS_CODES[code]))
                if 'x' in code:
                    self.response.out.write('\n')
        self.response.out.write('\n\nMore information about status codes can be found at %s\n' %
                                STATUS_CODES_DESCRIPTION_URL)
        self.response.write('For statuses out of the above reference please check %s\n' % WIKIPEDIA_CODES_DESCRIPTIONS_URL)
        self.response.write('Please have in mind that the codes from the Informational group - 1xx does not work due to Google App Engine restrictions')

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/(\d{3})?/?', MainPage)],
                              debug=True)