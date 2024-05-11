from ucimlrepo import fetch_ucirepo
from aids_project.data.schema import Patient

def migrate_1():
    source = fetch_ucirepo(id=890)
    df = source.data.original
    for _, row in df.iterrows():
        Patient.create(
            pidnum=row['pidnum'],
        cid =row['cid'],
        time =row['time'],
        trt =row['trt'],
        age =row['age'],
        wtkg =row['wtkg'],
        hemo =row['hemo'],
        homo =row['homo'],
        drugs =row['drugs'],
        karnof =row['karnof'],
        oprior =row['oprior'],
        z30 =row['z30'],
        zprior =row['zprior'],
        preanti =row['preanti'],
        race =row['race'],
        gender =row['gender'],
        str2 =row['str2'],
        strat =row['strat'],
        symptom =row['symptom'],
        treat =row['treat'],
        offtrt =row['offtrt'],
        cd40 =row['cd40'],
        cd420 =row['cd420'],
        cd80 =row['cd80'],
        cd820 =row['cd820'])


if __name__ == '__main__':
    migrate_1()

