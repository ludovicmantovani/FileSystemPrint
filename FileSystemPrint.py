#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET
import hashlib

def main():
    folderDict= dict()
    startingPath='.'
    rt = ET.Element("root")
    startingPathElement = ET.SubElement(rt,"node", type="folder")
    startingPathElement.text=startingPath
    folderDict[startingPath]=startingPathElement
    for root, dirs, files in os.walk(startingPath, topdown=True):
        for name in files:
            folderElement = folderDict[root]
            newFileElement = ET.SubElement(folderElement, "node", type="file")
            newFileElement.text=name.decode('utf-8')

        for name in dirs:
            fullFolderName = os.path.join(root, name)
            folderElement = folderDict[root]
            newFolderElement = ET.SubElement(folderElement, "node", type="Folder")
            newFolderElement.text=name.decode('utf-8')
            folderDict[fullFolderName] = newFolderElement

    tree = ET.ElementTree(rt)
    tree.write("filename.xml", encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
    main()

