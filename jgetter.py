# -*- coding:utf-8 -*-
"""
util for getting Java Jar version information
Why: getting latest jar version sometimes is annoying,
     open the browser,search for maven repository then input keyword to search.
     As a Mac User, complete these task in terminal is more nature.So comes this util.
How: use requests lib to get the search result, normal it is html file, then extract the
    use information to get it done. There are two major cases:
    1. only know the key words
    2. know the exactly java jar group id and artifact id
"""
from argparse import ArgumentParser

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

DEFAULT_MAVEN_REPO = "https://mvnrepository.com"


def artifact_url(group_id, artifact_id):
    """
    return the artifact url
    :param group_id:
    :param artifact_id:
    :return:
    """
    return "/".join([DEFAULT_MAVEN_REPO, 'artifact', group_id, artifact_id])


POM_DEP = """
<dependency>
    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
</dependency>

"""


def get_version(group_id, artifact_id):
    art_url = artifact_url(group_id, artifact_id)
    session = HTMLSession()
    result = session.get(art_url)
    versions = result.html.find(".release")
    print("the latest three versions are:")
    poms = []
    for version in versions[:3]:
        poms.append(POM_DEP.format(group_id=group_id, artifact_id=artifact_id, version=version.text))
    return poms


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-g", help="group id")
    parser.add_argument("-a", help="artifact id")
    arguments = parser.parse_args()
    poms = get_version(group_id=arguments.g, artifact_id=arguments.a)
    for pom in poms:
        print(pom)
