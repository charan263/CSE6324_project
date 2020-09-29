from Utils import XmlUtil
from Utils import Constants
from resource import TextResource
from xml.etree.ElementTree import Element, SubElement, Comment, tostring


class ColorWriter(TextResource.TextResource):

    def __init__(self):
        super().__init__()
#        self.mDocument = XmlUtil.createDocument();
        self.mRoot = Element(Constants.ELEMENT_RESOURCE)
        self.mDataIndexMap = {}
        self.mId = 0
        
    def addResource(self, color):

        _id = "color_"
        if color in self.mDataIndexMap:
            index = self.mDataIndexMap[color]
            _id = _id + str(index)
        else:
            _id = _id + str(self.mId)
            self.mDataIndexMap[color] = self.mId
            self.mId = self.mId + 1
            element = SubElement(self.mRoot, Constants.ELEMENT_COLOR)
            element.set(Constants.ATTRIBUTE_NAME, _id)
            element.text = color
        
        return _id
    