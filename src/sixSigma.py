import numpy as np

mu = 10
sigma = 3
size = 100000


# Cette fonction compte le nombre de points
# de cette distribution normale
# compris entre la moyenne et $n$ sigma.
def percentage_n_sigma(n_sigma, n_iter=1):
    counts = []
    for i in range(0, n_iter):
        # s contient $n$ tirages aléatoires
        # suivant une distribution normale
        # avec une moyenne de 10 et un écart-type de 3.
        s = np.random.normal(mu, sigma, size)
        countSigma = 0
        for e in s:
            countSigma += 1 if abs(e - mu) < n_sigma * sigma else 0
        counts += [countSigma]
    return np.mean(counts)

count1Sigma = percentage_n_sigma(1)
print(count1Sigma * 100 / size)
#> 68.54

count2Sigma = percentage_n_sigma(2)
print(count2Sigma * 100 / size)
#> 95.33

count3Sigma = percentage_n_sigma(3)
print(count3Sigma * 100 / size)
#> 99.71

count6Sigma = percentage_n_sigma(6)
print(count6Sigma * 100.0 / size)
#>100.0


# Quelques outliers sont introduits
# dans la distribution.
s = list(np.random.normal(mu, sigma, size)) + [100, 1000, 333]

# le filtrage a 6 sigma permet de les retrouver.
one_sigma_outliers = [x for x in s if abs(x-mu) >= 6 * sigma]
print(one_sigma_outliers)
#> [100, 1000, 333]

def normality_test(samples, mu, sigma, n_sigma):
    countSigma = 0
    for e in s:
        countSigma += 1 if abs(e - mu) < n_sigma * sigma else 0
    return countSigma / len(samples)

# Une distribution uniforme
# ne passe pas le test de normalité
# basé sur les $n$ sigma.
u = list(np.random.uniform(1, 10, size))
mu = np.mean(u)
sigma = np.std(u)

print(normality_test(u, mu, sigma, 1))
#> 0.25403
print(normality_test(u, mu, sigma, 2))
#> 0.59365
print(normality_test(u, mu, sigma, 3))
#> 0.86571
