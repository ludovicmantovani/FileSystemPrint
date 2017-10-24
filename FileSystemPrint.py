#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

def readConfig(inputFile):
    global nom_fichier
    nom_fichier = ''
    global starting_path
    starting_path = ''
    with open(inputFile,"r") as lines:
        for line in lines:
            if line.startswith('NOM_FICHIER'):
                nom_fichier=line.split('=')[1].strip()
            if line.startswith('STARTING_PATH'):
                starting_path=line.split('=')[1].strip()

def main():
    readConfig("configFSP")
    folderDict= dict()
    if starting_path == '':
        startingPath='.'
    else:
        startingPath = starting_path
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
    if nom_fichier == '':
        filename='out'
    else:
        filename=nom_fichier
    tree = ET.ElementTree(rt)
    tree.write(filename+".xml", encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
    main()

