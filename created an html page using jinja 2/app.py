import numpy as np
from jinja2 import Template
import pandas as pd
from pandas import DataFrame as df
import sys
import matplotlib.pyplot as plt

error_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Something Went Wrong</title>
</head>
<body>
<h1> Wrong Inputs</h1>
<p>Something went wrong</p>

</body>
</html>"""

students_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Data</title>
</head>
<body>
<h1>Student Details</h1>
<table border="1px">
    <thead>
    <tr>
        <td>Student id</td>
        <td>Course id</td>
        <td>Marks</td>
    </tr>
    </thead>
    <tbody>        
    {% for i in range(0,count)%}
        <tr>
            <td>{{output_in_dict['Student id'][i] }}</td>
            <td>{{output_in_dict[' Course id'][i] }}</td>
            <td>{{output_in_dict[' Marks'][i] }}</td>
        </tr>
        {% endfor %}
        <tr>
            <td colspan="2" align="center">
                Total Marks
            </td>
            <td> {{sum}}</td>
        </tr>
    </tbody>
</table>

</body>
</html>"""

course_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Course Data</title>
</head>
<body>
<h1>Course Details</h1>
<table border="1px">
    <thead>
        <tr>
            <td>Average Marks</td>
            <td>Maximum Marks</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                {{Avg}}
            </td>
            <td>{{Max}}</td>
        </tr>
    </tbody>
</table>
<img src = 'hist.png' >
</body>
</html>"""
rawdata = pd.read_csv("data.csv")

def main():
    try:
        type_of_data = sys.argv[1] #wheteher this is course or subject
        data_value = sys.argv[2]
        data = pd.DataFrame.from_dict(rawdata)
        if (type_of_data == "-s"):
            final_output = data[data['Student id'] == int(data_value)]
            total = final_output[' Marks'].sum()
            output_in_dict = final_output.to_dict('list')
            count = len(output_in_dict[' Marks'])
            if(count == 0):
                raise Exception
            TEMPLATE = students_html
            template = Template(TEMPLATE)
            content = template.render(output_in_dict = output_in_dict,count = count,sum = total)
            return content
        elif (type_of_data == "-c"):
            final_output = data[data[' Course id'] == int(data_value)]
            avg = final_output[' Marks'].mean()
            max = final_output[' Marks'].max()
            output_in_dict = final_output.to_dict('list')
            count = len(output_in_dict[' Marks'])
            if (count == 0):
                raise Exception
            hist = final_output.hist(column=' Marks')
            plt.savefig("hist.png")
            TEMPLATE = course_html
            template = Template(TEMPLATE)
            content = template.render(Avg = avg,Max = max)
            print(content)
            return content
        else:
            raise Exception
    except:
        #opening the errorpage and read

        TEMPLATE = error_html
        template = Template(TEMPLATE)
        content = template.render()
        return content


if __name__ == "__main__":
    main()






