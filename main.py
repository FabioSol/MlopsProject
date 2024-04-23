from model.predict import model_predict
from optimization import hyperparam_optimization


def main():
    best_params, report, cm = hyperparam_optimization()

    print("Best params: ", best_params)
    print(report)
    print(cm)

    prediction = model_predict([[10140.0, #pidnum
                   1181.0, #time
                   1.0, #trt
                   46.0,# age
                   88.9056,#wtkg
                   0.0,#hemo
                   1.0,#homo
                   1.0,#drugs
                   100.0,#karnof
                   0.0, #oprior
                   1.0,#z30
                   1.0,#zprior
                   1181.0,#preanti
                   0.0,# race
                   1.0,#gender
                   1.0,#str2
                   3.0,#strat
                   0.0,#symptom
                   1.0,#treat
                   0.0,#offtrt
                   235.0,#cd40
                   339.0,#cd420
                   860.0,#cd80
                   1060.0]]*2)#cd820
    print("example output")
    print(prediction)

if __name__ == '__main__':
    main()

