# Rule-based diagonostic system for five diseases

def diagnose_disease():
    diseases = {
        'Malaria': {'fever', 'chills', 'headache', 'nausea'},
        'Typhoid': {'prolonged fever', 'abdominal pain', 'diarrhea'},
        'Diabetes': {'frequent urination', 'excessive thirst', 'fatigue'},
        'Pneumonia': {'cough with phlegm', 'chest pain', 'difficulty breathing'},
        'Hypertension': {'high blood pressure', 'headaches', 'dizziness'},
    }
    print('Enter your symptoms (comma-separated): ')
    user_input = input().lower()
    user_symptoms = set(user_input.split(', '))

    possible_disease = []
    for disease, symptoms in diseases.items():
        match_count = len(user_symptoms.intersection(symptoms))
        if match_count >= len(symptoms) // 2:
            possible_disease.append(disease)

    if possible_disease:
        print('\nPossible Diagnosis: ')
        for disease in possible_disease:
            print(f'- {disease}')
    else:
        print('\nNo clear diagnosis found. Consider consulting a doctor.')
diagnose_disease()