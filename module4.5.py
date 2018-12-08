#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, send_from_directory, render_template
import pandas as pd

import flask

from flask import redirect, url_for, request

# create the application object
app = Flask(__name__)

env = pd.read_csv("2015StreetTreesCensus_TREES.csv")

envdata = env.iloc[:,[8,10,11,30]]

envdata.describe()

envdata1 = env.iloc[:,[8,10,30]]

con = envdata1.groupby(['boroname','spc_common','health'])['spc_common'].count().unstack(fill_value = 0).reset_index()

con1 = envdata1.groupby(['boroname','health'])['boroname'].count().unstack(fill_value = 0).reset_index()

fnameDict = {'Plants':con["spc_common"].tolist() }

df = pd.DataFrame(fnameDict)

df.reset_index(inplace=True)

df.columns = ['Abra', 'Plants']

con.drop(con.columns[[0,1]],axis =1,inplace = True)

lol = con.values.tolist()



dropdown_options = [
            {'label': df['Plants'][i] , 'value':df['Abra'][i]} for i in range(655)]



@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
