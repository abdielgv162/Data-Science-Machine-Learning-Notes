def calc_bayes(prior_A, prob_B_dado_A, prob_B): #Definimos el terorema de Bayes en una función
    return ( (prior_A * prob_B_dado_A) / prob_B )


if __name__ == '__main__': #Definimos la entrada del código para correrlo en la consola

    # Usando la tablita del notebook
    # https://i.imgur.com/7lXaJg6.pnghttps://i.imgur.com/7lXaJg6.png

    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    #Ejecutamos
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    print(prob_cancer_dado_sintoma)