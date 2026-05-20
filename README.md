# NLP Course — Natural Language Processing

**Universidad Carlos III de Madrid (UC3M)**
Department of Signal Theory and Communications

Professors: Angel Navia Vázquez, Pablo Martínez Olmos, Vanessa Gómez Verdejo, Emilio Parrado Hernández, Harold Molina Bulla

Student: **Matvey Sinelnik**

---

## Overview

Repository containing all materials, notebooks, and projects for the **Natural Language Processing** course in the Telecommunications Engineering degree at UC3M. The course spans from Python fundamentals to advanced NLP techniques: linguistic preprocessing, document vectorisation, supervised classification, syntactic analysis, word/text embeddings, and topic modelling with LDA.

All notebooks have been adapted for **local execution** (macOS, external drive) with a Python 3.10 virtual environment.

---

## Execution Environment

- **Python**: 3.10 (venv `nlp_env_2026`)
- **Jupyter Kernel**: `NLP 2026`
- **Core libraries**: NumPy 2.2.6, Pandas 2.3.3, SciPy 1.15.3, SpaCy 3.8.11, Gensim 4.4.0, NLTK 3.9.3, WordCloud 1.9.6, pyLDAvis 3.4.1, scikit-learn 1.7.2, Matplotlib 3.10.8

---

## Repository Structure

### Session 1 — Introduction to Python, NumPy, Matplotlib and Pandas

| Notebook | Content |
|----------|---------|
| `1_1_IntroPython1.ipynb` | Python fundamentals |
| `1_2_Workingwithlibraries.ipynb` | Libraries, I/O, modules and OOP |
| `1_3_Introduction_to_Numpy_and_Matplotlib.ipynb` | NumPy arrays and Matplotlib plotting |
| `1_4_Introduction_to_Pandas.ipynb` | Pandas DataFrames and data manipulation |

**`1_1_IntroPython1.ipynb`** covers the core pillars of the language: numeric types (`int`, `float`), arithmetic and compound assignment operators (`+=`, `*=`), math functions from the `math` module, boolean variables and comparison operators (`==`, `!=`, `<`, `>`), logical operators (`and`, `or`, `not`), and strings with their main methods (`.capitalize()`, `.upper()`, `.lower()`, `.replace()`, `.strip()`, `.find()`, `.split()`, `.join()`). It covers string indexing (slicing with `[start:end:step]`), concatenation, and formatting with `format()` and escape characters (`\n`, `\t`, `\"`). Control structures follow: `if/elif/else` conditionals, `while` loops (with `break`, `continue`, `else`) and `for` loops (with `range()` and `enumerate()`). The four fundamental Python collections are covered: lists (mutable, ordered, with `append()`, `insert()`, `remove()`, `pop()`, `del`, `clear()`), tuples (immutable, ordered, with `count()` and `index()`), sets (unordered, no duplicates, with `add()`, `update()`, `union()`, `remove()`, `discard()`) and dictionaries (key-value pairs, with `.get()`, `.items()`, `.keys()`, `.values()`, `.update()`, `.pop()`). Nested structures and list/dictionary comprehensions with `if/else` conditions are practised. Finally, user-defined functions are introduced along with the difference between pass-by-value and pass-by-reference.

**`1_2_Workingwithlibraries.ipynb`** covers module importing (`import`, `from ... import`, aliasing with `as`), package installation with `pip`, and file handling with `open()`, `write()`, `read()` in text and binary modes. It introduces serialisation with **Pickle** (`.dump()`/`.load()` for persisting Python objects) and MATLAB file interoperability via `scipy.io` (`loadmat`/`savemat`). It explains how to create custom modules (`.py` files with reusable functions) and packages (directories with `__init__.py`). The session concludes with an introduction to **Object-Oriented Programming**: class definition with `__init__`, attributes, methods, and inheritance for extending base classes (example: `HUMANS` → `PROFESSIONAL` → `TEACHER`/`STUDENT`).

**`1_3_Introduction_to_Numpy_and_Matplotlib.ipynb`** introduces **NumPy** as the foundation for scientific computing in Python. It covers array creation from lists, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, and random generators (`np.random.randn`). The distinction between 1D arrays (vectors) and 2D arrays (matrices) is explained via `.shape` and `.ndim`, along with dimension manipulation using `flatten()`, `ravel()`, `reshape()`, `np.newaxis`, and `np.squeeze()`. Indexing and slicing covers row/column selection with `[row, col]` syntax, boolean indexing with conditions, and `np.where()` for conditional element access. Array concatenation is done with `np.hstack()` and `np.vstack()`. Element-wise operations (`+`, `-`, `*`, `/`, `np.exp()`, `np.log()`, `np.sqrt()`) are distinguished from matrix operations: `np.dot()` / `@` for matrix multiplication, `np.linalg.inv()` for inversion, `np.linalg.det()` for determinants, `np.linalg.pinv()` for the Moore-Penrose pseudoinverse, and `.T` for transposition. Broadcasting rules are demonstrated for operations between arrays of different shapes. Data persistence is shown with Pickle serialisation. The **Matplotlib** section covers random data generation from various distributions (`np.random.randn`, `np.random.uniform`, `np.random.exponential`), line plots and scatter plots with `plt.plot()` and `plt.scatter()`, figure customisation (labels, titles, legends, colours, markers, line styles), histograms with `plt.hist()` (relative frequencies, bin control, density estimation), bar plots, subplot arrays with `plt.subplots()`, text annotations, contour plots with `plt.contour()`/`plt.contourf()`, and 3D surface plots with `plot_surface()`.

**`1_4_Introduction_to_Pandas.ipynb`** introduces the **Pandas** library for structured data manipulation. It loads the Kaggle house prices dataset from CSV with `pd.read_csv()` into a DataFrame, which is the core Pandas data structure. Column access is demonstrated both as dictionary-style (`data['column']`) and attribute-style, including multi-column selection with lists. Column operations cover renaming (`.rename()`), statistical aggregation (`.mean()`, `.std()`, `.min()`, `.max()`, `.median()`), and custom transformations using `.apply()` with lambda functions (example: converting square feet to square metres). Column removal is done with `.drop()`. The three main indexing methods are explained in depth: `iloc` for integer-position-based selection (rows and columns by numeric index, supporting slices like `[1:5]`), `loc` for label-based selection (by index value, supporting boolean/conditional filtering like `data.loc[data['Quality'] == 'Good']`), and chained conditions with `&` and `|` operators. Missing data handling covers detection with `pd.isnull()` and `.apply()` across columns to count NaN values, with references to imputation strategies. The Matplotlib integration section demonstrates scatter plots, histograms, and multi-panel figures directly from DataFrames. Data export covers `to_csv()` for CSV output, Excel file support, and conversion to NumPy arrays with `.values`.

---

### Session 2 — Text Preprocessing with NLTK and SpaCy

| Notebook | Content |
|----------|---------|
| `2_1_Preprocesado_texto_SpaCy_espan_ol.ipynb` | Full linguistic preprocessing pipeline |

This session presents the text processing pipeline needed to transform raw text into numerical representations suitable for Machine Learning. It works with the NLTK `movie_reviews` corpus (2000 movie review documents labelled as positive/negative), accessed through the `CorpusReader` object and its methods (`fileids`, `categories`, `raw`).

**Preprocessing** is structured in several stages. **Tokenisation** (splitting text into individual tokens) is first done with basic string methods (`.split()`) and then with NLTK (`sent_tokenize` for sentences, `word_tokenize` for words), which correctly handles punctuation marks and special cases. **Homogenisation** comprises: lowercase conversion, punctuation removal, **stemming** (reducing words to their root by suffix trimming, with NLTK's `PorterStemmer` — fast but may produce non-words like "studi" from "studies") and **lemmatisation** (reducing to the canonical dictionary form while preserving valid words, using linguistic models). The removal of **stop words** (function words without semantic content: "the", "a", "for", "and"...) is explained.

**SpaCy** is introduced as a production-grade NLP library. A pre-trained model (`en_core_web_md`) is loaded, which runs an automatic pipeline on text, generating iterable `Doc` objects composed of `Token` objects with key attributes: `text`, `lemma_`, `pos_` (Part of Speech), `tag_` (fine-grained tag), `dep_` (syntactic dependency), `is_alpha`, `is_digit`, `is_stop`, `is_punct`. These attributes are visualised in Pandas tables and each POS tag is explained with `spacy.explain()`. SpaCy for **Spanish** is demonstrated with the `es_core_news_sm/md` models, trained on the AnCora annotated corpus.

The final normalisation function combines all steps: for each token in a document, its lowercase lemma is retained only if it is alphabetic, not a stop word, and has length > 1. This is applied to the entire corpus, and `Counter` from `collections` is used to compute word frequencies. Exercises include extracting the 20 most frequent adjectives and locating contiguous verb+noun pairs sorted by frequency.

---

### Session 3 — Document Vectorisation and Clustering

| Notebook | Content |
|----------|---------|
| `3_1_Vectorizacion_y_agrupamiento_de_documentos_con_Gensim_NLTK_y_SKlearn.ipynb` | BoW, TF-IDF, K-Means with cosine distance |

Works with the NLTK `inaugural` corpus (US presidential inaugural addresses). After applying the preprocessing from the previous session, the vocabulary is built with **Gensim** (`corpora.Dictionary`), which automatically generates a word→id mapping along with frequency statistics: `cfs` (collection frequency: total occurrences of each word across the corpus) and `dfs` (document frequency: number of documents containing the word).

**Vocabulary management** is critical for controlling dimensionality. Filters are applied with `filter_extremes()`: `no_below` (minimum number of documents a word must appear in to be retained), `no_above` (maximum document proportion — removes overly common words), and `keep_n` (retain only the top N most frequent words after filtering). `filter_tokens(bad_ids=[...])` is available for removing specific words. Frequency distributions before and after filtering are visualised, showing the typical Zipf distribution.

**Bag of Words vectorisation** is done with `doc2bow()`, which transforms each document (list of tokens) into a list of `(word_id, count)` tuples in sparse format. The **TF-IDF representation** (Term Frequency–Inverse Document Frequency) reweights the counts: TF measures local term frequency in a document, and IDF penalises terms appearing in many documents (IDF = log(N_docs / N_docs_with_term)). It is implemented with Gensim's `TfidfModel`, which fits on the full BoW corpus and then transforms each document.

The **limitations of BoW and TF-IDF** are discussed: loss of word order, inability to capture semantics and synonyms, and very high-dimensional vectors. For computing **document similarities**, the inadequacy of Euclidean distance (depends on document length) is explained, and **cosine similarity** (cos(θ) = (v₁·v₂)/(‖v₁‖·‖v₂‖)) is introduced, which measures the angle between vectors regardless of magnitude.

Format conversion uses `matutils.corpus2dense()` (for dense NumPy arrays) and `matutils.corpus2csc()` (for SciPy CSC sparse matrices), the latter being preferred for large corpora.

**K-Means clustering** is implemented two ways: with NLTK (which supports cosine distance directly but not sparse matrices) and with sklearn (which requires prior L2 normalisation of vectors, since for normalised vectors minimising Euclidean distance equals maximising cosine similarity). Clusters from BoW and TF-IDF are compared, analysing which documents/speeches fall into each group.

---

### Session 4 — Keyword Extraction and Text Summarisation

| Notebook | Content |
|----------|---------|
| `4_1_extraccion_de_palabras_clave_y_resumen_de_textos.ipynb` | LSA, TextRank, RAKE, collocations |

Works on a long Wikipedia text (Gears of War video game description). The text is segmented into sentences using SpaCy's `doc.sents` (which returns a generator, not an indexable list). The difference between generators and iterables is explained, along with `itertools.islice` and `next` for partial access.

The **TF-IDF matrix** is built treating each sentence as a "document" within the text. Terms are filtered with `filter_extremes` (minimum 2 sentences, maximum 80% of sentences).

**Latent Semantic Analysis (LSA)** uses Singular Value Decomposition (SVD) of the TF-IDF matrix: A ≈ U·S·Vᵀ. The U matrix (terms × topics) describes each word's contribution to each latent topic. The V matrix (topics × sentences) describes the topical composition of each sentence. S (diagonal) contains singular values weighting each topic's importance. A rank-k approximation is applied (retaining only the k largest singular values), reducing noise and dimensionality. The **saliency score** of each sentence is computed as the norm of the corresponding row vector in G = Vᵀ·S, weighted by a threshold on singular values (as proposed by Steinberger & Ježek). Sentences with the highest saliency scores form the text summary.

**TextRank** applies the PageRank algorithm on a graph where nodes are sentences and edge weights are TF-IDF cosine similarities between them. It is implemented with `networkx.pagerank()`. PageRank assigns greater importance to sentences that are similar to many other important sentences, capturing the document's semantic centrality.

**RAKE** (Rapid Automatic Keyword Extraction) extracts candidate keywords by splitting text into phrases delimited by stop words and punctuation. For each word, its degree (connections in the co-occurrence matrix) and frequency are computed, and each keyword's score is the sum of degree/frequency ratios of its constituent words. Implemented with the `rake-nltk` library.

**Collocations** identify word sequences that co-occur more frequently than expected by chance. Bigrams, trigrams, and quadgrams are extracted using `nltk.collocations` with association measures like PMI (Pointwise Mutual Information).

---

### Session 5 — Machine Learning Fundamentals: Classification

| Notebook | Content |
|----------|---------|
| `5_1_-_Fundamentos_ML_Clasificacion.ipynb` | Logistic Regression, k-NN, metrics, ROC and PR curves |

Introduces supervised Machine Learning applied to text classification. Using synthetic 2D data, **Logistic Regression (LR)** is visualised: a linear model estimating P(y=1|x) = σ(wᵀx + w₀) where σ is the sigmoid function. The decision boundary (hyperplane where P=0.5), the **Log Loss** cost function (binary cross-entropy), and how different weight vectors produce different separations are explained.

**Regularisation** is introduced to prevent overfitting: a penalty term on weight magnitude (L1 or L2) is added, controlled by hyperparameter C (inverse of regularisation strength) in sklearn. Optimal C is selected via **N-fold cross-validation** with `GridSearchCV`.

Everything is applied to the **Spam dataset** (4601 observations, 57 continuous variables derived from word and character frequencies). LR is trained with C selection by cross-validation, and model weights are analysed to identify which words contribute positively or negatively to spam detection.

The **k-NN classifier** is presented as a non-parametric alternative: it classifies by majority vote among the k nearest neighbours. Overfitting with k=1 (100% train accuracy, worse on test) and the complexity of the non-linear decision boundary are observed.

**Binary classification metrics** are explained in detail from the confusion matrix (TP, FP, TN, FN): FPR (False Positive Rate), TNR/Specificity, FNR (False Negative Rate), TPR/Recall/Sensitivity, Precision, and F1-score (harmonic mean of P and R). The **ROC curve** (TPR vs FPR as the decision threshold varies, with AUC as the global metric) and the **Precision-Recall curve** (especially useful with imbalanced classes) are generated. It is demonstrated that no single threshold optimises all metrics simultaneously.

---

### Session 6 — Text Analysis: POS Tagging and NER

| Notebook | Content |
|----------|---------|
| `6_Text_analysis_techniques_POS_tagging__NER.ipynb` | POS tagging, chunking, Matcher, NER, dependency parsing |

Presents structural text analysis techniques that go beyond bag-of-words representations.

**POS tagging** (Part-of-Speech tagging) assigns each token its lexical category (noun, verb, adjective, determiner...) based on syntactic context. SpaCy implements neural network-based models achieving high accuracy. Key attributes: `pos_` (universal category: NOUN, VERB, ADJ...), `tag_` (fine-grained tag: NN, VBD, JJ...) and `dep_` (syntactic role: nsubj, dobj, ROOT...). SpaCy's ability to distinguish "engineer" as noun or verb depending on context is demonstrated.

**Shallow Parsing / Chunking** groups adjacent tokens into phrases by function: Noun Phrases (NP), Verb Phrases (VP), Prepositional Phrases (PP), Adjective Phrases (ADJP) and Adverb Phrases (ADVP). SpaCy provides `doc.noun_chunks` for direct NP chunking. For other patterns, SpaCy's **Matcher** class is used, allowing rules based on lexical attributes (TEXT, POS, LEMMA, IS_ALPHA, IS_DIGIT, LENGTH, OP for quantifiers like *, +, ?). It is applied to "Alice in Wonderland" from NLTK's Gutenberg corpus to locate patterns like "Alice + verb + object".

**NER (Named Entity Recognition)** identifies and classifies named entities: PERSON, ORG, GPE (geopolitical entities), DATE, MONEY, PRODUCT, EVENT, etc. SpaCy implements state-of-the-art algorithms. Entities are visualised with `displacy.render()` which generates colour-coded annotations. It is applied to the complete Gutenberg books to extract the list of all mentioned characters.

**Dependency Parsing** extracts the syntactic dependency tree of each sentence, identifying relationships between words (subject, direct object, modifiers...). The root (ROOT) is typically the main verb. SpaCy provides tree visualisation with `displacy` in "dep" mode, and attributes like `children`, `lefts`, `rights` and `subtree` for programmatic tree traversal. Sentences where the root is a verb are identified and the subject of each action is extracted.

---

### Session 7 — Word and Text Embeddings

| Notebook | Content |
|----------|---------|
| `7_Word_Text_embeddings.ipynb` | Word2Vec, Skip-Gram, SpaCy embeddings, LSA for sentences, doc embeddings |

Introduces **embeddings** as dense, low-dimensional vector representations (96-300 dims vs thousands in BoW), where semantically similar words occupy nearby positions in vector space. The limitations of one-hot representations (high dimensionality, no notion of similarity) and BoW/TF-IDF (loss of order and semantics) are explained.

The **Word2Vec (Skip-Gram)** model is explained from its foundations: starting with a review of binary logistic regression (σ(wᵀx), cross-entropy cost function) and its **multiclass** extension (softmax: P(y=k|x) = exp(zₖ)/Σexp(zⱼ)). Skip-Gram uses a sliding window over text to generate (centre word, context word) pairs. The architecture is a two-layer neural network: the input layer encodes the centre word with one-hot (dimension V = vocabulary size), the hidden layer produces a D-dimensional vector (the embedding), and the output layer uses softmax to predict context words. The **input weight matrix W** (V×D) contains the word embeddings: each word's row is its learned vector representation.

**Pre-trained SpaCy embeddings** are accessed via the `token.vector` attribute (available in `md` and `lg` models). Euclidean distances and cosine similarities between words are computed (Rome-Paris closer than Rome-apple). The **Reuters** corpus from NLTK (10877 financial news articles, 90 categories) is used, with normalisation and vocabulary reduction. An embedding dictionary is built to speed up nearest-word searches (reducing execution time from seconds to milliseconds).

Other models are presented: **CBoW** (Continuous Bag of Words: predicts the centre word from context, inverse of Skip-Gram), **GloVe** (Global Vectors: combines global co-occurrence statistics with local learning), and **FastText** (extends Word2Vec using character n-grams, enabling embeddings for out-of-vocabulary words).

For **sentence/text embeddings**, three approaches are implemented: (1) **LSA** (SVD of the sentence-level TF-IDF matrix, using G = Vᵀ·S as each sentence's representation), (2) **mean word embeddings** (averaging word vectors per sentence, directly with SpaCy's `doc.vector`), and (3) **Doc2Vec** (Word2Vec extension that learns a per-document vector). Cosine similarity matrices between all Reuters corpus sentences are computed and compared: LSA produces zero similarity between sentences with no shared vocabulary, while word embeddings capture semantic similarities between different but related words.

---

### Session 8 — Topic Modelling with LDA

| Notebook | Content |
|----------|---------|
| `8_Topic_models_LDA_student.ipynb` | LDA, coherence metrics, pyLDAvis, PCA exercises |

Introduces **Topic Modelling** as an unsupervised method for discovering the latent thematic structure of a corpus. Explained as a probabilistic extension of LSA.

**Latent Dirichlet Allocation (LDA)** is presented as a generative probabilistic model using plate notation: each document m has a topic distribution θₘ (drawn from a Dirichlet with parameter α), each word in the document is generated by first selecting a topic z according to θₘ and then a word according to the topic's word distribution φₖ (also Dirichlet, with parameter β). Training seeks the posterior distribution given observed words, typically via **Variational Bayes** or **Gibbs Sampling**.

Applied to the **NeurIPS papers** dataset (1428 articles from 2019-2020, concatenating title and abstract). After SpaCy normalisation and vocabulary filtering (1586 terms), an LDA model is trained with Gensim (`LdaMulticore`). Model functionalities are explored: `show_topics()` displays the most probable words per topic with weights, `get_document_topics()` gives the topic distribution per document, and `get_topics()` returns the full topic×word matrix.

**WordCloud visualisation** generates word clouds coloured by topic. Each document's representation as a topic mixture (K-dimensional vector with positive weights summing to 1) is converted to a dense matrix with `corpus2dense()`.

**Topic number selection** uses **coherence metrics** (via Gensim's `CoherenceModel`): **C_UCI** (based on PMI of co-occurring word pairs) and **C_NPMI** (normalised version). Models from 3 to 50 topics are evaluated, finding an optimum at **7 topics** for both metrics.

Model persistence uses both **Pickle** (generic Python serialisation) and Gensim's native `save()`/`load()` functions (generating multiple files: `.lda`, `.lda.state`, `.lda.id2word`, `.lda.expElogbeta.npy`). Integrity is verified by comparing the original and loaded models.

**Interactive visualisation with pyLDAvis** generates an HTML with: intertopic distance map (PCA 2D of topics, with areas proportional to word count), and term relevance panel per topic (controlled by λ, which interpolates between absolute frequency and term exclusivity).

**Supplementary exercises** include: (1) identifying the most representative document for each topic (maximum weight in the corresponding column of the doc×topic matrix), and (2) 2D PCA visualisation of both topics in word space and documents in topic space, coloured by dominant topic.

---

### Session 9 — Introduction to Neural Networks with PyTorch

| Notebook | Content |
|----------|---------|
| `9_Intro_a_NNs_con_Pytorch.ipynb` | Artificial neurons, MLPs, backpropagation, PyTorch tensors and autograd |

This session is the gateway from classical ML to deep learning. It starts with the **biological motivation** (Santiago Ramón y Cajal's drawings, dendrites as inputs, synapses as weights, axon as output) and the **McCulloch–Pitts artificial neuron** (1943): a weighted sum of inputs `x_i` with weights `w_i` plus a bias, passed through a non-linear activation function. The classical activations are introduced — **sigmoid** σ(z) = 1/(1+exp(-z)), **tanh**, and **ReLU** = max(0, z) — and the move toward ReLU in deep networks is justified (no vanishing gradients in the positive regime, faster computation).

**Multilayer Perceptrons (MLPs)** generalise Rosenblatt's perceptron to multiple stacked layers. The **error backpropagation** algorithm (Rumelhart, Hinton & Williams, *Nature* 1986) is explained as the efficient way to compute partial derivatives of the loss with respect to all weights via the **chain rule**, propagating gradients backward through the network. Loss surfaces in neural networks are non-convex with multiple local minima; gradient descent finds a nearby one.

**PyTorch** is then introduced as the framework that makes all of this practical via **automatic differentiation**. The `torch.Tensor` data type is presented as NumPy-like but with two key features: it can live on GPU/MPS, and it tracks the computation graph for autograd. Tensor creation (`torch.zeros`, `torch.ones`, `torch.randn`, `torch.tensor`), reshaping (`.view`, `.reshape`, `.flatten`), element-wise vs matrix operations (`torch.matmul`/`@`/`torch.mm`), and the bidirectional conversion with NumPy (`torch.from_numpy`, `.numpy()`) are practised.

**Logistic Regression in PyTorch** is built from scratch in three increasingly compact forms:
1. **Manual implementation** using bare tensor operations and a `sigmoid()` function.
2. **A custom `nn.Module` class** with attributes `self.weights` and `self.bias` and a `forward()` method.
3. **A compact form** using predefined layers — `nn.Linear(in_features, out_features)` followed by `nn.Sigmoid()` (or, more numerically stable, `nn.Linear` + `BCEWithLogitsLoss` which fuses sigmoid and binary cross-entropy).

It is applied to the **Spam dataset** (4601 obs, 57 features). The training loop is built piece by piece: (a) the **Binary Cross-Entropy** cost, (b) the `requires_grad=True` flag and gradient accumulation, (c) the `.backward()` call that fills `.grad` attributes via autograd, (d) `optim.SGD`/`Adam` optimisers, and (e) the canonical training step — `optimizer.zero_grad()` → forward → `loss.backward()` → `optimizer.step()`. The loop is encapsulated in a class that combines the model definition and the `.fit()` method.

---

### Session 10 — Deep Learning: Regularisation and Convolutional Networks

| Notebook | Content |
|----------|---------|
| `10_Aprendizaje_Profundo_DL.ipynb` | Deep MLPs, regularisation, CNN layers, LeNet5 on Fashion-MNIST, autoencoders, CNNs for text |

The session opens with the conceptual difference between shallow and deep models: **stacking layers produces hierarchical internal representations** (edges → textures → object parts → objects in vision; phonemes → words → phrases in audio; characters → words → semantics in text). Geoffrey Hinton's definition of deep learning is cited, and the historical landmarks are reviewed — LeCun's digit-recognition model (1989), **LeNet** (1998, first CNN with formal "convolution" and "subsampling" layers), and **AlexNet** (2012, 60M parameters, won ImageNet, introduced ReLU, dropout and GPU training at scale).

**The training protocol** (train/validation/test split) is formalised, and the two failure modes are diagnosed: **high variance** (train loss much lower than validation loss → overfitting; remedies are more data, simpler model, regularisation) and **high bias** (both losses high → underfitting; remedies are more capacity or better features). Three concrete **regularisation techniques** are implemented:

1. **Early stopping**: monitor the validation loss across epochs and stop when it begins to rise. Implemented as a class extension of the previous `MLP_train`, computing `valid_loss` every epoch and keeping the best-so-far weights.
2. **Dropout**: random deactivation of activations during training (each unit kept with probability *p*). Reduces co-adaptation of features and acts as an implicit ensemble. Implemented with `nn.Dropout` layers in the MLP.
3. **Data augmentation**: synthesise new training samples by transforming existing ones (image rotations, crops, flips; for text: synonym replacement, back-translation). Demonstrated with the `torchvision.transforms` pipeline on Fashion-MNIST.

**Convolutional layers** are introduced as the alternative to fully-connected layers when the input has spatial structure. The session covers each layer type in turn: **`Conv2d`** (sliding kernels of size *M×M* over the input, producing *P* feature maps, with parameters *stride*, *padding* and *dilation*), **pooling** (`MaxPool2d`, `AvgPool2d` — local downsampling that reduces spatial dimensions and adds translation invariance), **flatten** (tensor → 1D vector to feed dense layers), **fully-connected**, and the final **softmax** layer for multiclass classification. The dataset used is **Fashion-MNIST** (60 000 train + 10 000 test, 28×28 grey-scale images, 10 classes), downloaded via `torchvision.datasets`.

**LeNet5** is implemented end-to-end as a class: two conv+pool blocks followed by three fully-connected layers, trained with cross-entropy loss and Adam, reaching ~90% test accuracy on FMNIST. Extension exercises include computing the **confusion matrix**, adding a `.predict()` method, and scaling to the full training set.

**Autoencoders and pre-training** are introduced as an unsupervised way to learn good initial representations: a network is trained to reconstruct its input through a low-dimensional bottleneck; the encoder weights then serve as initialisation for a downstream classifier. Finally, **CNNs for text** are discussed: 1D convolutions sliding over word embeddings act as learned n-gram detectors, an alternative to RNNs for sequence classification.

---

### Session 11 — Recurrent Neural Networks (RNN, LSTM)

| Notebook | Content |
|----------|---------|
| `11_Redes_neuronales_recurrentes_RNNs.ipynb` | Sequential processing, RNNs, vanishing gradient, LSTMs, sentiment classification on Financial PhraseBank |

The session addresses the structural problem of feeding text to a feed-forward network: **inputs of variable length** and the need to **preserve order**. The different input/output configurations are catalogued — *one-to-one* (classification), *one-to-many* (image captioning), *many-to-one* (sentiment from a sentence), *many-to-many* synchronous (POS tagging) and *many-to-many* asynchronous (translation, summarisation). The need for a model that consumes tokens **sequentially while maintaining an internal state** motivates RNNs.

**The vanilla RNN** updates a hidden state `h_t = tanh(W_x · x_t + W_h · h_{t-1} + b)` and produces an output `y_t = g(W_y · h_t)`. The **temporal unfolding** (unrolling) of the network into a single graph is explained, and the cost is defined as the sum of per-step losses. Two operating modes are distinguished: **non-iterated** (final output after consuming the full sequence — for classification) and **generative** (the prediction is fed back as the next input — the basis of language modelling). The **vanishing gradient problem** is explained: gradients backpropagated through many time steps multiply repeatedly by derivatives of saturating activations, so the signal becomes too small to update early weights — i.e. the RNN cannot learn long-range dependencies.

**LSTMs** (Hochreiter & Schmidhuber, 1997) solve this with a **gating mechanism**: an additional **cell state `C_t`** that carries information across time with minimal multiplicative interference, plus three **gates** that learn what to add, what to forget and what to read:
- **Forget gate** `f_t = σ(W_f · [h_{t-1}, x_t] + b_f)` — decides which parts of the cell state to drop.
- **Input gate** `i_t = σ(...)` combined with a candidate `Ĉ_t = tanh(...)` — adds new information.
- **Output gate** `o_t = σ(...)` — produces the hidden state from the cell state, `h_t = o_t · tanh(C_t)`.

The complete LSTM equations are derived and implemented in PyTorch with `nn.LSTM`, with attention to the input/output tensor shapes `(seq_len, batch, features)` and the optional `batch_first=True` flag.

**Practical application — sentiment classification on Financial PhraseBank** (financial news headlines, three classes negative/neutral/positive, **highly imbalanced**). Five models are trained and compared side by side, with results stored as pickles for reuse in Session 12:
1. **TF-IDF + LR** baseline.
2. **Mean document embeddings + LR** (averaging SpaCy word vectors per sentence).
3. **Doc embeddings + kNN**.
4. **Doc embeddings + MLP** (three-layer classifier in PyTorch).
5. **Word embeddings + LSTM + LR head** — the sequential model.

For each model, accuracy, precision, recall, F1 and the **confusion matrix** are reported. The imbalance is addressed by reporting the **majority-class baseline** explicitly. Extension exercises explore hyperparameter tuning.

---

### Session 12 — Transformers

| Notebook | Content |
|----------|---------|
| `12_Transformers_student.ipynb` | Attention, self-attention, Q/K/V, multi-head, positional encoding, BERT, RoBERTa, FinBERT, machine translation |

This session presents the architecture that powers modern NLP. The motivation is twofold: (a) **a complete understanding of a sentence requires a global view of all tokens simultaneously**, which sequential processing cannot provide; (b) to scale to very large models on very large corpora, training must be **parallelisable across the sequence dimension**, again impossible with RNNs that process one step at a time.

**The original encoder–decoder Transformer** (Vaswani et al., *Attention Is All You Need*, 2017) is introduced for machine translation: the encoder produces a contextual representation of every source token; the decoder generates the target sequence one token at a time, attending to both the encoder output (**cross-attention**) and its own previous outputs (**masked self-attention**). The three usage patterns are catalogued: **encoder-only** (BERT, RoBERTa — for classification and NER), **decoder-only** (GPT family — for generation), and **encoder-decoder** (T5, M2M100 — for translation, summarisation).

**Attention mechanisms** are the core innovation. The session explains **self-attention** (relating different positions of the same sequence — used to enrich each word's representation with information from its neighbours), **cross-attention** (between two sequences — e.g. decoder attending to encoder), and **causal/masked self-attention** (decoder attending only to past tokens during generation).

**Scaled dot-product attention** is derived step by step:
1. Each token's embedding **X** (shape `n × d`) is linearly projected into **Q** (queries — *what am I looking for?*), **K** (keys — *what do I contain?*) and **V** (values — *what information do I carry?*).
2. The affinity matrix is `F = Q · Kᵀ / √d_k` (the `√d_k` prevents the softmax from saturating for large `d_k`).
3. A row-wise **softmax** turns `F` into attention weights.
4. The output is `Attention(Q, K, V) = softmax(Q · Kᵀ / √d_k) · V`.

**Multi-head attention** stacks `H` parallel attention modules (each with its own Q/K/V projections, often with `d_k = d / H`), concatenates the outputs, and applies a final linear projection. Each head learns to focus on a different kind of relation (syntactic, semantic, positional).

**Positional encoding** restores order information lost by the permutation-equivariant attention layer. The original sinusoidal encoding `PE(pos, 2i) = sin(pos / 10000^{2i/d})` is explained, along with the more recent **learned positional embeddings** and **rotary positional embeddings (RoPE)**.

The **complete Transformer block** is assembled — multi-head self-attention → residual + layer-norm → feed-forward network (two linear layers with GELU) → residual + layer-norm — stacked *N* times (*N=6* in the original paper).

**BERT** (Bidirectional Encoder Representations from Transformers) is then explained: pre-trained on **Masked Language Modeling** (predict randomly masked tokens) and **Next Sentence Prediction**, producing bidirectional contextual embeddings. The `[CLS]` token's representation is used for sentence-level classification.

**Practical application — sentiment classification with pre-trained models** on the same Financial PhraseBank used in Session 11 (same split for fair comparison):
- **BERT base** (`bert-base-uncased`) fine-tuned via the Hugging Face `transformers` library.
- **RoBERTa** (`cardiffnlp/twitter-roberta-base-sentiment-latest`) — a model already fine-tuned for sentiment.
- **FinBERT** (`ProsusAI/finbert`) — domain-specific model pre-trained on financial texts.

Each model is evaluated with **accuracy, precision, recall, F1, ROC AUC** and **decision-threshold optimisation** (extension exercise). FinBERT wins on this corpus, illustrating the value of domain-adapted pre-training.

**Machine translation** is demonstrated with **Helsinki-NLP/Opus-MT** (English → German, English → Spanish), and with Meta's **M2M100** (`facebook/m2m100_418M` and `1.2B`) — a single 100-language many-to-many model. Extension exercises automate translation to all supported languages and analyse failure cases (low-resource pairs).

---

### Session 13 — Large Language Models (LLMs)

| Notebook | Content |
|----------|---------|
| `13_LLMs.ipynb` | LLM fundamentals, model size taxonomy, SmolLM2, Phi-3.5-mini, GGUF/llama.cpp, LM Studio, frontier models |

This session ties everything together by presenting the current state of generative language models. A **language model** is defined as a system that, given an input sequence (prompt), predicts the most probable next token, iterating to produce coherent text. Modern LLMs are almost always **decoder-only Transformers**: they apply multiple layers of masked self-attention over a context window, with a final linear projection over the vocabulary.

The session distinguishes the **two training phases**:
1. **Pre-training** on massive unlabelled corpora (web text, books, code, articles) by next-token prediction. The model learns grammar, world knowledge, code, reasoning patterns — adjusting billions of parameters.
2. **Fine-tuning** to convert the raw next-token predictor into a helpful assistant: **supervised fine-tuning (SFT)** on instruction–response pairs, then **alignment** with **RLHF** (Reinforcement Learning from Human Feedback) or **DPO** (Direct Preference Optimisation) to make the model follow instructions, refuse harmful requests and adopt a specific style.

The main **capabilities** of LLMs are listed: text generation, summarisation, translation, code writing, chain-of-thought reasoning, and tool use. The session emphasises that these capabilities emerge from scale and broad pre-training — they are not explicitly programmed.

A **model-size taxonomy** is presented with the hardware footprint of each tier:
| Tier | Parameter range | Example | Hardware |
|---|---|---|---|
| **Nano / Micro** | < 1B | SmolLM2-360M | Smartphone, IoT |
| **Small (SLM)** | 1B – 10B | Phi-3.5-mini-instruct (3.8B), Llama 3.2 3B | Consumer laptop |
| **Medium** | 10B – 50B | Llama 3 8B, Gemma 2 27B | High-end GPU |
| **Large (LLM)** | 50B – 300B | Llama 3 70B, Qwen 72B | Multi-GPU server cluster |
| **Frontier** | > 300B (often MoE) | GPT-4, Claude 4, Gemini Ultra | Datacenter supercomputer |

Practical **inference examples**:
- **SmolLM2-360M-Instruct** is loaded via Hugging Face `transformers` to demonstrate small-model behaviour on a set of evaluation queries ("¿Cuál es la capital de Francia?", arithmetic, code completion). The limitations of nano models in reasoning are made explicit.
- **Phi-3.5-mini-instruct (3.8B)** is run locally through **`llama.cpp`** using the **GGUF** quantised format. GGUF is presented as the de-facto standard for local LLM deployment: a single binary file that bundles weights (typically quantised to 4-bit or 5-bit), tokeniser, and metadata, runnable on CPU or modest GPUs.
- **LM Studio** is introduced as a graphical desktop tool to download, manage and chat with local GGUF models.
- A reflection on **frontier models** closes the session: they outperform all earlier tiers on reasoning benchmarks, but a vast number of practical applications can be solved adequately (and far more cheaply) by SLMs running locally — a recurring theme in current NLP practice.

---

## Projects

### Project 1 — Text Classification: "crude" News Detector

| Notebook | Content |
|----------|---------|
| `Proyecto_1_NLP_CrudeClasiffier.ipynb` | Binary classification with TF-IDF + LR and DistilBERT fine-tuning |

The goal is to classify news from the **Reuters-21578** corpus (NLTK) as belonging or not to the "crude" category (crude oil and petroleum markets). Two approaches are implemented:

**Phase 1 — TF-IDF + Logistic Regression**: SpaCy preprocessing (tokenisation, lemmatisation, stop word removal), TF-IDF vectorisation, and classification with regularised Logistic Regression (C selection by cross-validation). Model weights are analysed to identify the most discriminative words (positive → associated with "crude", negative → discriminate against "crude"). Evaluation with full metrics: accuracy, precision, recall, F1-score, ROC curve and Precision-Recall curve.

**Phase 2 — DistilBERT Fine-tuning**: Transfer learning fine-tuning of the pre-trained DistilBERT model (distilled version of BERT, transformer-based) to capture contextual relationships that TF-IDF cannot represent. Both approaches are compared in terms of precision, recall, and the trade-off shown in the PR curve.

---

### Project 2 — Duplicate Question Detection (Quora)

| Notebook | Content |
|----------|---------|
| `Proyecto_2_NLP_QuoraDuplicates.ipynb` | TF-IDF, LSA, Sentence Transformers, Precision@K |

Works with a 10000-pair subset from the **Quora Question Pairs** dataset, where each pair indicates whether two questions are semantically duplicates. The goal is, given a question, to find its duplicate among the others using vector similarity.

Three **vectorisation methods** are implemented:

1. **TF-IDF** with word n-grams (1,2) and character n-grams (2,4) to capture both lexical matches and morphological subword patterns.

2. **LSA** (Latent Semantic Analysis) applying truncated SVD over the TF-IDF matrix to obtain reduced-dimension dense representations capturing latent semantic structure.

3. **Sentence Transformers** (text embeddings): pre-trained models generating dense full-sentence embeddings, capturing deep semantic relationships via transformer architectures.

For each method, the **cosine distance matrix** between all question pairs is computed and evaluated with **Precision@K**: for each question, it is verified whether its true duplicate appears among the K nearest results. The three methods are compared, observing that transformer embeddings outperform TF-IDF and LSA in capturing non-lexical semantic similarities, while TF-IDF excels at exact vocabulary matches.

---

### Project 3 — Opinion Analysis (Binary Sentiment Classification)

| Notebook | Content |
|----------|---------|
| `Proyecto_3_NLP_AnalisisOpinion.ipynb` | Classical baselines + DistilBERT fine-tuning (first iteration) |
| `Proyecto_3_NLP_AnalisisOpinion_FINAL.ipynb` | **Deliverable version**: leakage-free pipelines, homogeneous 5-fold CV, DistilBERT 5-fold OOF, stacking, full test diagnostics |

Binary classification of opinion (positive = 1, negative = 0) over a **mixed multi-domain corpus** (8 000 training samples, 2 000 test, ~48 % positive class) combining four very different sources: **tweets** (airline complaints, Apple/tech), **drug reviews** (clinical vocabulary), **financial news** (Reuters/Finnish corporations) and **other web text**. The mix is detected with a lightweight heuristic and used to break down results per domain.

**Final pipeline (deliverable notebook).** All models share the **same** evaluation protocol — `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` with **ROC AUC** — and every transformation lives **inside an sklearn `Pipeline`/`FeatureUnion`** so the cross-validation is leakage-free (the TF-IDF vocabulary and the meta-feature scaler are fit only on each train fold).

Eight models are compared:
1. **LR + TF-IDF word** on SpaCy-lemmatised text — light baseline.
2. **LR + TF-IDF word+char** on lightly-cleaned text that preserves `!`, `?` and capitalisation (signals critical for sentiment that the first iteration discarded).
3. **Calibrated LinearSVC** + TF-IDF word+char.
4. **MultinomialNB** + TF-IDF word+char.
5. **LR + TF-IDF word+char + meta-features**: VADER scores (pos/neg/neu/compound), upper-case ratio, `!`/`?` counts, negation flag (`not`, `no`, `never`…) and TextBlob polarity, combined via `FeatureUnion` and standardised inside the pipeline.
6. **LR optimised by `GridSearchCV`** over the regularisation strength.
7. **DistilBERT fine-tuned with 5-fold CV** (`distilbert-base-uncased`, `max_len=192`, 2 epochs, batch 16, LR 2e-5). Each fold model is saved to disk for ensemble inference on test; **Out-Of-Fold (OOF)** probabilities are concatenated to give a fair, comparable AUC.
8. **Stacking** — a meta-`LogisticRegression` trained on the OOF probabilities of DistilBERT, LR(word+char) and LR(word+char+meta). Because all three base features are OOF, the stacker is trained without leakage and its CV AUC is honest.

**Winner selection** is automatic: the model with the highest 5-fold AUC is declared winner. The stacker is then deployed on test:
1. DistilBERT predictions are the average of the five fold models (ensemble).
2. LR(word+char) and LR(word+char+meta) are re-trained on 100 % of the training set.
3. The three probabilities are stacked and passed through the meta-LR.

**Test diagnostics** (the deliverable section that was missing in the original iteration):
- Final stacker AUC on test, plus per-component AUC for diagnostic purposes.
- **Confusion matrix** and `classification_report` at threshold 0.5.
- **ROC curve** for the stacker and the three components.
- **AUC broken down by domain** (tweet / drug_review / financial / other) — exposing where the model is strongest and weakest.
- **Top-10 highest-confidence errors** for qualitative inspection.

The notebook is designed to run end-to-end in a **single execution of 40–45 minutes** on an Apple M2 Pro with MPS (DistilBERT is the dominant cost). The first-iteration notebook is kept for reference; the `_FINAL` version is the one to grade.

---

## Supplementary Material

The `8_MaterialComplementario/` folder contains artefacts generated during Session 8:

- `papers.csv` — NeurIPS papers dataset
- `best_topic_model_Neurips.pkl` — Optimal LDA model (7 topics) serialised with Pickle
- `best_topic_model_Neurips.lda*` — LDA model in native Gensim format
- `LDAvis_best_model.html` — Interactive pyLDAvis visualisation

---

## Notes

- Notebooks were originally designed for Google Colab. References to `google.colab` and `drive.mount()` have been replaced with local paths.
- The file `papers.zip` (>100 MB) is excluded from the repository via `.gitignore` as it exceeds GitHub's file size limit.
- Transformer fine-tuning runs (Project 1 DistilBERT, Project 3 DistilBERT, Session 12 BERT/RoBERTa/FinBERT) use the Apple Silicon GPU through the PyTorch **MPS** backend (`torch.device("mps")`). The corresponding model directories (`distilbert_*/`, `roberta_*/`) contain training checkpoints and should be re-generated locally.
- All thirteen course sessions and the three projects are now documented in this README.
