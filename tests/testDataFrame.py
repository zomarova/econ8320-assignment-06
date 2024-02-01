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

    def testDataFrame(self):
      columns = ['date', 'Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio',
       'Occupancy']
       
      test = True

      for i in columns:
        if i not in occupancy.columns:
          test = False

      self.assertTrue(test, "Your columns don't match the columns in the answer key.")