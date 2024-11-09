import xml.sax


handle = xml.sax.ContentHandler()

parser = xml.sax.make_parser()

parser.setContentHandler(handle)

parser.parse("group.xml")


class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        print(name)


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("group.xml")


