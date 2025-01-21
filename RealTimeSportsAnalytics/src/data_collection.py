import random

def collect_data():
    try:
        data = {
            'speed': random.uniform(20, 30),  # Simulated speed in km/h
            'distance': random.uniform(90, 110),  # Simulated distance in meters
            'heart_rate': random.randint(140, 160)  # Simulated heart rate
        }
        return data
    except Exception as e:
        print(f"Error collecting data: {e}")
        return None
