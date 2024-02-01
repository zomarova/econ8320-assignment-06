import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def testSteamyCol(self):
      answer = pd.read_csv("tests/answerPandas.csv")

      self.assertTrue(answer['steamy'].equals(occupancy['steamy']), "Your 'steamy' column is not correctly constructed.")
