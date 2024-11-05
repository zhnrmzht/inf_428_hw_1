import unittest
import numpy as np

def generate_random_data(mean, variance, num_samples):
    data = np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)
    print(f"Generated data (mean: {mean}, variance: {variance}): {data}")
    return data

def calculate_aggregated_threat_score(data):
    total_score = 0
    total_weight = 0
    for dept in data:
        dept_mean_score = np.mean(dept['scores'])
        weight = dept['importance']
        total_score += dept_mean_score * weight
        total_weight += weight
        print(f"Department mean score: {dept_mean_score}, Importance: {weight}")
    aggregated_score = min(90, total_score/total_weight) if total_weight > 0 else 0
    print(f"Total Score: {total_score}, Total Weight: {total_weight}, Aggreagted Score: {aggregated_score}")
    return aggregated_score

class TestScoreCalculation(unittest.TestCase):
    def test_equal_importance_uniform_scores(self):
        data = [
            {'scores': generate_random_data(45, 5, 50), 'importance': 3},
            {'scores': generate_random_data(45, 5, 50), 'importance': 3},
            {'scores': generate_random_data(45, 5, 50), 'importance': 3},
            {'scores': generate_random_data(45, 5, 50), 'importance': 3},
            {'scores': generate_random_data(45, 5, 50), 'importance': 3}
        ]
        result = calculate_aggregated_threat_score(data)
        print(f"Test result (Equal Importance & Uniform Scores): {result}")
        self.assertAlmostEqual(result, 45, delta=10)

    def test_varying_importance(self):
        data = [
            {'scores': generate_random_data(30, 5, 50), 'importance': 5},
            {'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'scores': generate_random_data(30, 5, 50), 'importance': 2},
            {'scores': generate_random_data(30, 5, 50), 'importance': 4},
            {'scores': generate_random_data(30, 5, 50), 'importance': 1}
        ]
        result = calculate_aggregated_threat_score(data)
        print(f"Test result (Varying Importance): {result}")
        self.assertAlmostEqual(result, 30, delta=10)

    def test_high_outlier_department(self):
        data = [
            {'scores': generate_random_data(85, 5, 50), 'importance': 5},
            {'scores': generate_random_data(30, 5, 50), 'importance': 3},
            {'scores': generate_random_data(20, 5, 50), 'importance': 2},
            {'scores': generate_random_data(25, 5, 50), 'importance': 4},
            {'scores': generate_random_data(15, 5, 50), 'importance': 1},
        ]
        result = calculate_aggregated_threat_score(data)
        print(f"Test result (High Outlier Department): {result}")
        self.assertGreater(result, 40)

    def test_low_importance_high_threat(self):
        data = [
            {'scores': generate_random_data(10, 5, 50), 'importance': 5},
            {'scores': generate_random_data(20, 5, 50), 'importance': 4},
            {'scores': generate_random_data(15, 5, 50), 'importance': 3},
            {'scores': generate_random_data(75, 5, 50), 'importance': 1},
            {'scores': generate_random_data(10, 5, 50), 'importance': 2}
        ]
        result = calculate_aggregated_threat_score(data)
        print(f"Test result (Low Importance High Threat): {result}")
        self.assertLess(result, 35)

if __name__ == '__main__':
    unittest.main()