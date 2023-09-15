from prophet import Prophet
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from flask import Flask,request, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dash.html')

@app.route('/linearRE', methods=['POST'])
def linearRE():
    feature1 = float(request.form['rev'])
    feature2 = float(request.form['emp'])

    df = pd.read_csv('models\kuehne_causal(csv).csv')

    X = df[['revenue', 'employee']] 
    y = df[['emissions', 'energy', 'water', 'waste']]  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train)

    new_data = pd.DataFrame({'revenue': [feature1], 'employee': [feature2]})
    predicted_values = rf_regressor.predict(new_data)

    for i in range(0,4):
        predicted_values[0][i] = round(predicted_values[0][i],2)

    return render_template('dash.html', pred=predicted_values[0][0], pred1=predicted_values[0][1], pred2=predicted_values[0][2], pred3=predicted_values[0][3])

@app.route('/upload_and_predict', methods=['POST'])
def upload_and_predict():
    file = request.files['file']
    if not file:
        return "No file uploaded"

    df = pd.read_csv(file)
    period = int(request.form.get("period"))

    forecast_data = []
    chart_paths = []
    for column in df.columns[1:]:
        df_prophet = df[['year', column]].rename(columns={'year': 'ds', column: 'y'})
        df_prophet = df_prophet.dropna()

        model = Prophet()
        model.fit(df_prophet)
        future = model.make_future_dataframe(periods=period, freq='y')
        forecast = model.predict(future)
        forecast_data.append({'parameter': column, 'forecast': forecast[['ds', 'yhat']]})

        plt.figure()
        plt.plot(forecast['ds'].shift(+1), forecast['yhat'])
        plt.xlabel('Year')
        plt.ylabel('Forecast Value')
        plt.title(f'{column} Forecast')

        chart_path = f'static/chart_{column}.png'
        plt.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)

    return render_template('dash.html', forecast_data=forecast_data, chart_paths=chart_paths)

if __name__ == '__main__':
    app.run()