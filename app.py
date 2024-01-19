from flask import Flask, Response
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
    return "Welcome to the Prometheus Flask exporter!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
