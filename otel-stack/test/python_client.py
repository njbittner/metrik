import time

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Create an exporter for the metrics
exporter = OTLPMetricExporter(endpoint="localhost:4317", insecure=True)

# Create a meter provider and add a periodic exporting metric reader
meter_provider = MeterProvider(metric_readers=[PeriodicExportingMetricReader(exporter)])
metrics.set_meter_provider(meter_provider)

# Get a meter
meter = metrics.get_meter(__name__, version="1.0")

# Create a counter metric
counter = meter.create_counter(
    "my_counter",
    description="A simple counter",
    unit="1",
)

# Record some metrics
for i in range(100):
    print(f"Recording metric {i}")
    counter.add(1, attributes={"environment": "production"})
