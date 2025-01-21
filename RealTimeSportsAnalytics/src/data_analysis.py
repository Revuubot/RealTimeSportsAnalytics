def analyze_data(data):
    performance_score = (data['speed'] * 0.5) + (data['distance'] * 0.3) - (data['heart_rate'] * 0.2)
    return {'performance_score': performance_score}
