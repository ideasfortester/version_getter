# -*- coding:utf-8 -*-
from unittest import TestCase

from jgetter import artifact_url, get_version


class TestPJavaJarGetter(TestCase):
    def test_artifact_url(self):
        result = artifact_url(group_id="org.testng", artifact_id="testng")
        self.assertEqual(result, "https://mvnrepository.com/artifact/org.testng/testng")

    def test_get_version(self):
       result= get_version(group_id="org.testng", artifact_id="testng")
       self.assertTrue(len(result)>0)
