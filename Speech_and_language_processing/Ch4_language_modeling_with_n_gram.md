# Ch4 Language Modeling with N-grams

> Models that assign probabilities to sequences of words are called language models or LMs. 


## 4.1 N-Grams
> The simplest model that assigns probabilities to sentences and sequences of words, the N-gram.

一串文本长度为$N$，表示为$w^n_1$

其概率为$P(w_1,w_2,w_3,...,w_n)$

$ P(X_1 ... X_n)=P(X_1)P(X_2|X_1)P(X_3|X^2_1)...P(X^n|X^{n-1}_1) $
$ =\prod_{k=1}^{n}P(X_k|X^{k-1}_1) $

#### bigram
我们难以计算完整的概率，而是仅使用最近的n个词，来获取一个<u>近似</u>的概率.
例如，某个词跟在前序词后的概率可以近似表达为$ P(w_n|w_1) $

The assumption that the probability of a word depends only on the previous word is called a **Markov** assumption. Markov models are the class of probabilistic models that assume we can predict the probability of some future unit without looking too far into the past. We can generalize the bigram (which looks one word into the past) to the trigram (which looks two words into the past) and thus to the N-gram (which looks N − 1 words into the past).

#### trigram, 4-gram, 5-gram
Although for pedagogical purposes we have only described bigram models, in practice it’s more common to use trigram models, which condition on the previous two words rather than the previous word, or 4-gram or even 5-gram models, when there is sufficient training data. Note that for these larger N- grams, we’ll need to assume extra context for the contexts to the left and right of the

#### log-probabilities

## 4.2 Evaluating Language Models
> 实践是检验真理的唯一标准。

#### extrinsic evaluation 外在评估 v.s. intrinsic evaluation 内在评估
外部评估效果固然好，但是代价昂贵。
内在评估是ML最常用的做法, 将训练集拆分为train set, test set

### 4.2.1 Perplexity (PP)
Perplexity其实表示的是average branch factor，大概可以翻译为平均分支系数。即平均来说，我们预测下一个词时有多少种选择。

举个例子来说，对于一个长度为N的，由0-9这10个数字随机组成的序列。由于这10个数字随机出现，所以每个数字出现的概率是$ \frac{1}{10} $。也就是，在每个点，我们都有10个等概率的候选答案供我们选择，于是我们的perplexity就是10（有10个合理的答案）

$$ PP(W)= \sqrt[N]{\frac{1}{P(w_1w_2...w_N)}}  $$

另一种常用的perplexity表达形式如下（以unigram为例）： 

$$ PP(S)=2^{-\frac1{N}\sum{log(P(w_i))}} $$

其中，$N$ 是句子 $S$ 的长度，$P(w_i)$ 是第 $i$ 个词的概率（如果是bigram就应该是第i个bigram的概率）
这个式子是从交叉熵的角度推导出来，很多地方讲perplexity的时候就用的这个式子。

