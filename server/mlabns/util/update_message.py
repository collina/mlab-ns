import logging

from . import message

class UpdateMessage(message.Message):

    def __init__(self):
        message.Message.__init__(self)
        self.tool_id = None
        self.slice_id = None
        self.server_id = None
        self.sliver_ipv4 = None
        self.sliver_ipv6 = None
        self.status = None
        self.url = None

        self.required_fields = set([
            message.SERVER_ID,
            message.SITE_ID,
            message.SLICE_ID,
            message.SLIVER_IPv4,
            message.SLIVER_IPv6,
            message.STATUS,
            message.TOOL_ID,
            message.URL])

    def initialize_from_dictionary(self, dictionary):
        for field in self.required_fields:
            if field not in dictionary:
                raise FormatError('Missing field %s.' % (field))

        self.tool_id = dictionary[message.TOOL_ID]
        self.slice_id = dictionary[message.SLICE_ID]
        self.server_id = dictionary[message.SERVER_ID]
        self.site_id = dictionary[message.SITE_ID]
        self.sliver_ipv4 = dictionary[message.SLIVER_IPv4]
        self.sliver_ipv6 = dictionary[message.SLIVER_IPv6]
        self.status = dictionary[message.STATUS]
        self.url = dictionary[message.URL]

        if message.TIMESTAMP in dictionary:
            self.timestamp = dictionary[message.TIMESTAMP]

        if message.SIGNATURE in dictionary:
            self.signature = dictionary[message.SIGNATURE]

    def to_dictionary(self):

        dictionary = {}
        dictionary[message.SITE_ID] = self.site_id
        dictionary[message.SERVER_ID] = self.server_id
        dictionary[message.SIGNATURE] = self.signature
        dictionary[message.SLICE_ID] = self.slice_id
        dictionary[message.SLIVER_IPv4] = self.sliver_ipv4
        dictionary[message.SLIVER_IPv6] = self.sliver_ipv6
        dictionary[message.STATUS] = self.status
        dictionary[message.TIMESTAMP] = self.timestamp
        dictionary[message.TOOL_ID] = self.tool_id
        dictionary[message.URL] = self.url

        return dictionary