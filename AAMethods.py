class AAMethods:
    '''
    Chapter 3 talks about three language models.
    The most plausible one is context-free grammars(CFGs) that groups words according to grammatical categories,
    which is most often used to capture long-range structural dependencies.
    Less complex ones can be like Markov chains that assumes words before and after a specific word should be relatively stable.
    It can be used to capture short-range structural dependencies.
    The easiest one is to form a large collection of words with their frequency of appearance.
    Later in this chapter, it talked about the concept of Shannon entropy and cross entropy,
    Kolmogorov complexity which are all related to the authorship.
    Chapter 5 talked about how to analyze these attributes to determine the authorship.
    There’re two kind of methods,
    the first one is unsupervised analysis which do not require the documents to be sorted and categorized by human,
    but supervised analysis do. In unsupervised analysis, vector spaces could be used to represent the result.
    To keep the graph in two dimensions, PCA is used which is the eigenvectors of the covariance matrix that can be used to represent variation of data.
    Other methods include MDS which uses cross-entropy and cluster analysis,
    which is similar to MDS but reduces the numbers of items by grouping them together.
    Supervised Analysis include statistical analysis, linear discriminant analysis and distance-based analysis.
    '''
    pass
