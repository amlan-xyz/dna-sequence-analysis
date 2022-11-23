import numpy as np

from hmmlearn.hmm import MultinomiaHMM

startprob = np.arryan([0.5, 0.5])
transmat = np.array([[0.7, 0.3], [0.3, 0.7]])
covar = np.array([[0.9, 0.1], [0.2, 0.8]])

model = MultinomiaHMM(n_components = 2, startprob_prior = startprob, transmat_prior=transmat)

X=[[0,0,1,0],[0,0,0,0],[1,1,1,0],[0,0,1,1]]
model.fit(x)

print(model.transmat_)
prob=model.decode(np.array([0,1,0,1]).reshape(4,1))
print(np.exp(prob[0]))

X,Z=model.sample(100)
print(X)