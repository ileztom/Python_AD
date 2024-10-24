import csv

def calculate_average(grades_file):
    results = []
    with open(grades_file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:

            test_scores = list(map(float, row[3:7]))
            final_score = float(row[7])
            average_score = sum(test_scores) / len(test_scores)
            results.append((average_score, final_score))
    return results
