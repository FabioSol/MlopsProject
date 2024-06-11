import requests


def main():
    from faker import Faker
    import random

    fake = Faker()

    def generate_fake_data(num_samples):
        fake_data = []
        for _ in range(num_samples):
            patient = {
                "pidnum": fake.random_number(digits=5),
                "time": random.randint(1, 100),
                "trt": random.randint(0, 1),
                "age": random.randint(18, 90),
                "wtkg": random.uniform(40, 150),
                "hemo": fake.boolean(),
                "homo": fake.boolean(),
                "drugs": fake.boolean(),
                "karnof": random.randint(20, 100),
                "oprior": fake.boolean(),
                "z30": fake.boolean(),
                "zprior": fake.boolean(),
                "preanti": random.randint(0, 3),
                "race": fake.boolean(),
                "gender": fake.boolean(),
                "str2": fake.boolean(),
                "strat": random.randint(1, 5),
                "symptom": fake.boolean(),
                "treat": fake.boolean(),
                "offtrt": fake.boolean(),
                "cd40": random.randint(0, 10),
                "cd420": random.randint(0, 10),
                "cd80": random.randint(0, 10),
                "cd820": random.randint(0, 10)
            }
            fake_data.append(patient)
        return fake_data

    X=generate_fake_data(1)[0]
    print(X)
    print(requests.post("http://localhost:8000/predict/",json=X).json())

if __name__ == '__main__':
    main()

