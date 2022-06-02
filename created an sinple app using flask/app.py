from flask import Flask, request
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route("/" , methods =['GET','POST'])
def DisplayData():
    try:
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            type_of_data = request.form['ID']
            data_value = request.form['id_value']
            rawdata = pd.read_csv("data.csv")
            data = pd.DataFrame.from_dict(rawdata)
            if (type_of_data == "student_id"):
                final_output = data[data['Student id'] == int(data_value)]
                total = final_output[' Marks'].sum()
                output_in_dict = final_output.to_dict('list')
                count = len(output_in_dict[' Marks'])
                if (count == 0):
                    raise Exception
                content = render_template('StudentDetails.html',output_in_dict=output_in_dict, count=count, sum=total)
                return content
            elif (type_of_data == "course_id"):
                print('working')
                final_output = data[data[' Course id'] == int(data_value)]
                avg = final_output[' Marks'].mean()
                max = final_output[' Marks'].max()
                output_in_dict = final_output.to_dict('list')
                count = len(output_in_dict[' Marks'])
                if (count == 0):
                    raise Exception
                final_output.hist(column=' Marks')
                plt.savefig("static/abc.png")
                content = render_template('CourseDetails.html',Avg=avg, Max=max)
                return content
            else:
                raise Exception
    except:
        return render_template('Error.html')





if __name__ == '__main__':
    app.debug = True
    app.run()