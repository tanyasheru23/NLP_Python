class MarkovClassifier:
  def __init__(self, logAs, logpis, logpriors):
    self.logAs = logAs
    self.logpis = logpis
    self.logpriors = logpriors
    self.K = len(logpriors) # number of classes = len of priors

  def _compute_log_likelihood(self, input_, class_):
    logA = self.logAs[class_]
    logpi = self.logpis[class_]

    logprob = logpi[input_[0]] + sum((logA[input_[t-1]][input_[t]]) for t in range(1, len(input_)))
    return logprob

  def predict(self, inputs):
    preds = np.zeros(len(inputs))
    for i, input_ in enumerate(inputs):
      posteriors = [self._compute_log_likelihood(input_, c) + self.logpriors[c] for c in range(self.K)]
      pred = np.argmax(posteriors)
      preds[i] = pred

    return preds
