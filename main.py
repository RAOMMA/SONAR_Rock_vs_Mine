# import argparse
# import joblib

# model = joblib.load('C:/salman/ML/SONAR Rock vs Mine/logistic_regression_model.pkl')

# parser = argparse.ArgumentParser()
# parser.add_argument('-value', type=str, default="0.0411,0.0277,0.0604,0.0525,0.0489,0.0385,0.0611,0.1117,0.1237,0.2300,0.1370,0.1335,0.2137,0.1526,0.0775,0.1196,0.0903,0.0689,0.2071,0.2975,0.2836,0.3353,0.3622,0.3202,0.3452,0.3562,0.3892,0.6622,0.9254,1.0000,0.8528,0.6297,0.5250,0.4012,0.2901,0.2007,0.3356,0.4799,0.6147,0.6246,0.4973,0.3492,0.2662,0.3137,0.4282,0.4262,0.3511,0.2458,0.1259,0.0327,0.0181,0.0217,0.0038,0.0019,0.0065,0.0132,0.0108,0.0050,0.0085,0.0044")

# args = parser.parse_args()

# data = args.value

# data_list = [float(value) for value in data.split(",")]
# data_list = [data_list]
# pre = model.predict(data_list)[0]

# if pre == "R":
#     print("Rock")
# elif pre == "M":
#     print("Mines")








import argparse
import joblib

# Load the pre-trained logistic regression model
model = joblib.load('C:/salman/ML/SONAR Rock vs Mine/logistic_regression_model.pkl')

# Create an argument parser
parser = argparse.ArgumentParser(description="Rock-vs-Mine Classification")

# Add the --value argument to accept a data record
parser.add_argument('--value', type=str, required=True, help="Comma-separated feature values for classification")

# Parse the command-line arguments
args = parser.parse_args()

# Get the data record from the command-line argument
data_record = args.value

# Parse the data record as a list of floats
data_list = [float(value) for value in data_record.split(',')]

# Make a prediction using the loaded model
prediction = model.predict([data_list])

# Print the result
if prediction[0] == "R":
    print("Rock")
elif prediction[0] == "M":
    print("Mines")
else:
    print("Unknown class")
